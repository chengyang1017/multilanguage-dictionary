import os
import re
import json
import sqlite3
import pandas as pd

# ──────────── 配置目录 ────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data/raw_data")  # 源 Excel
DB_DIR = os.path.join(BASE_DIR, "data/db")             # 输出 DB
JS_FILE = os.path.join(BASE_DIR, "static/js/lang-schemas.js")
JSON_FILE = os.path.join(BASE_DIR, "static/js/lang-schemas.json")

os.makedirs(DB_DIR, exist_ok=True)

# ──────────── Step 1: JS -> JSON ────────────
with open(JS_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# 清理 JS，生成合法 JSON
text = re.sub(r"^const\s+LANG_SCHEMAS\s*=\s*", "", text.strip(), flags=re.M)
text = re.sub(r";\s*$", "", text)
text = re.sub(r"//.*", "", text)
text = re.sub(r"'([^']*)'", r'"\1"', text)
text = re.sub(r",(\s*[\]}])", r"\1", text)

try:
    LANG_SCHEMAS = json.loads(text)
except json.JSONDecodeError as e:
    print("❌ JSON 解析失败:", e)
    exit(1)

# 写入 JSON 文件（可选）
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(LANG_SCHEMAS, f, ensure_ascii=False, indent=4)

print(f"✅ JS 已转换为 JSON: {JSON_FILE}")

# ──────────── Step 2: 处理 Excel -> DB ────────────
for lang, classes in LANG_SCHEMAS.items():
    excel_file = os.path.join(RAW_DATA_DIR, f"{lang}_words.xlsx")
    db_file = os.path.join(DB_DIR, f"{lang}.db")

    if not os.path.exists(excel_file):
        print(f"⚠️ Excel 文件缺失: {excel_file}, 跳过 {lang}")
        continue

    print(f"\n📥 开始处理语言: {lang}")
    all_sheets = pd.read_excel(excel_file, sheet_name=None)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    lang_total_inserted = 0  # 语言总计

    for sheet_name, df in all_sheets.items():
        schema = classes.get(sheet_name)
        if not schema:
            print(f"⚠️ 忽略未配置 schema 的 sheet: {sheet_name}")
            continue

        table_name = f"{lang}_{sheet_name}_table"

        # 删除旧表并创建新表
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"""
            CREATE TABLE {table_name} (
                word TEXT PRIMARY KEY,
                meanings TEXT,
                type TEXT,
                data JSON
            )
        """)

        sheet_inserted = 0  # 当前 sheet 插入数

        for _, row in df.iterrows():
            word = next((row[k] for k in schema["section1"]["keys"] if k in row and pd.notna(row[k])), "未知")
            meanings = row.get("意思", "未命名") if "意思" in df.columns else "未命名"
            word_type = row.get("词性", "未知") if "词性" in df.columns else "未知"

            cursor.execute(
                f"INSERT OR REPLACE INTO {table_name} VALUES (?, ?, ?, ?)",
                (word, meanings, word_type, json.dumps(row.to_dict(), ensure_ascii=False))
            )
            sheet_inserted += 1

        lang_total_inserted += sheet_inserted
        print(f"  ✅ Sheet '{sheet_name}' 注入 {sheet_inserted} 条数据 -> 表: {table_name}")

    conn.commit()
    conn.close()
    print(f"🎯 {lang} 语言数据库更新完成，总注入 {lang_total_inserted} 条数据 -> {db_file}")
