import os
import re
import json
import sqlite3
import pandas as pd
import argparse  # 引入参数解析

# ──────────── 命令行参数配置 ────────────
parser = argparse.ArgumentParser(description="将 Excel 词库转换为 SQLite 数据库")
parser.add_argument("--lang", type=str, help="指定要更新的语言代码 (例如: en, jp)。不指定则更新全部。")
args = parser.parse_args()

# ──────────── 配置目录 ────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data/raw_data")
DB_DIR = os.path.join(BASE_DIR, "data/db")
JS_FILE = os.path.join(BASE_DIR, "static/js/lang-schemas.js")
JSON_FILE = os.path.join(BASE_DIR, "static/js/lang-schemas.json")

os.makedirs(DB_DIR, exist_ok=True)

# ──────────── Step 1: JS -> JSON (始终运行以确保 Schema 最新) ────────────
with open(JS_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# 清理 JS（这里保留你原有的正则逻辑）
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

with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(LANG_SCHEMAS, f, ensure_ascii=False, indent=4)

# ──────────── Step 2: 筛选处理范围 ────────────
# 如果指定了 --lang，则只保留该语言的配置
if args.lang:
    if args.lang in LANG_SCHEMAS:
        target_schemas = {args.lang: LANG_SCHEMAS[args.lang]}
        print(f"🚀 模式：单语言更新 -> [{args.lang}]")
    else:
        print(f"❌ 错误：在 lang-schemas.js 中找不到语言 '{args.lang}' 的配置")
        exit(1)
else:
    target_schemas = LANG_SCHEMAS
    print("🚀 模式：全量更新所有语言")

# ──────────── Step 3: 处理 Excel -> DB ────────────
for lang, classes in target_schemas.items():
    excel_file = os.path.join(RAW_DATA_DIR, f"{lang}_words.xlsx")
    db_file = os.path.join(DB_DIR, f"{lang}.db")

    if not os.path.exists(excel_file):
        print(f"⚠️ Excel 文件缺失: {excel_file}, 跳过 {lang}")
        continue

    print(f"\n📥 开始处理语言: {lang}")
    all_sheets = pd.read_excel(excel_file, sheet_name=None)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    lang_total_inserted = 0

    for sheet_name, df in all_sheets.items():
        schema = classes.get(sheet_name)
        if not schema:
            continue

        table_name = f"{lang}_{sheet_name}_table"
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"""
            CREATE TABLE {table_name} (
                word TEXT PRIMARY KEY,
                meanings TEXT,
                type TEXT,
                data JSON
            )
        """)

        sheet_inserted = 0
        for _, row in df.iterrows():
            # 获取单词逻辑
            word_keys = schema.get("section1", {}).get("keys", [])
            word = next((row[k] for k in word_keys if k in row and pd.notna(row[k])), "未知")
            
            meanings = row.get("意思", "未命名") if "意思" in df.columns else "未命名"
            word_type = row.get("词性", "未知") if "词性" in df.columns else "未知"

            cursor.execute(
                f"INSERT OR REPLACE INTO {table_name} VALUES (?, ?, ?, ?)",
                (word, meanings, word_type, json.dumps(row.to_dict(), ensure_ascii=False))
            )
            sheet_inserted += 1

        lang_total_inserted += sheet_inserted
        print(f"  ✅ Sheet '{sheet_name}' -> 表: {table_name} ({sheet_inserted} 条)")

    conn.commit()
    conn.close()
    print(f"🎯 {lang} 数据库更新完成。")