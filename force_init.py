import sqlite3
import os
import json

# 定位绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'databases', 'ru.db')
JSON_FILE_PATH = os.path.join(BASE_DIR, 'databases', 'ru_data.json')

def update_database():
    if not os.path.exists(JSON_FILE_PATH):
        print(f"❌ 找不到 JSON 文件: {JSON_FILE_PATH}")
        return

    try:
        # 1. 纯净读取
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            raw_data_list = json.load(f)

        # 2. 数据库连接
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # 3. 彻底重置表结构 (删除旧表残留)
        cursor.execute("DROP TABLE IF EXISTS ru_table")
        cursor.execute('''
            CREATE TABLE ru_table (
                word TEXT PRIMARY KEY,   
                meanings TEXT,           
                type TEXT,               
                data JSON                
            )
        ''')

        # 4. 批量注入
        for item in raw_data_list:
            # 核心逻辑：确定词头和基本属性
            word = item.get("未完成体不定式") or item.get("主格") or "未知"
            meanings = item.get("意思", "未命名")
            word_type = item.get("词性", "动词" if "不定式" in str(item) else "名词")

            cursor.execute(
                "INSERT OR REPLACE INTO ru_table VALUES (?, ?, ?, ?)",
                (word, meanings, word_type, json.dumps(item, ensure_ascii=False))
            )

        conn.commit()
        print(f"✅ 数据库刷新成功！共注入 {len(raw_data_list)} 条纯净数据。")

    except Exception as e:
        print(f"❌ 注入失败: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    update_database()