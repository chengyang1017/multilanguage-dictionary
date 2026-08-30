from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import json
import math

app = Flask(__name__)

# 数据库路径
DB_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/db')

def get_db_connection(lang):
    db_path = os.path.join(DB_FOLDER, f'{lang}.db')
    if not os.path.exists(db_path):
        return None
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def clean_value(value):
    """清理 NaN、numpy 类型，保证 JSON 可序列化"""
    if value is None:
        return ""
    if isinstance(value, float) and math.isnan(value):
        return ""
    return value

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/classic')
def classic():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    lang = request.args.get('lang', 'ru').lower()
    
    if not query:
        return jsonify({"success": False, "msg": "请输入内容"})

    try:
        conn = get_db_connection(lang)
        if conn is None:
            return jsonify({"success": False, "msg": f"{lang} 数据库不存在"}), 500
        cursor = conn.cursor()

        # 获取该数据库所有表
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row['name'] for row in cursor.fetchall() if row['name'].startswith(f"{lang}_")]
        if not tables:
            return jsonify({"success": False, "msg": f"{lang} 数据库没有表"}), 500

        results = []

        for table in tables:
            sql = f"""
                SELECT DISTINCT {table}.* FROM {table}, json_each({table}.data)
                WHERE {table}.word LIKE ?
                OR {table}.meanings LIKE ?
                OR json_each.value LIKE ?
            """
            search_param = f"%{query}%"
            cursor.execute(sql, (search_param, search_param, search_param))
            rows = cursor.fetchall()

            for row in rows:
                raw_data = row["data"]
                try:
                    details = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
                except Exception:
                    details = {}
                # 清理 JSON
                details = {k: clean_value(v) for k, v in details.items()}

                results.append({
                    "headword": clean_value(row["word"]),
                    "meanings": clean_value(row["meanings"]),
                    "type": clean_value(row["type"]),
                    "all_details": details,
                    "table": table  # 记录是哪个 sheet
                })

        print(f"[后端] 请求 query='{query}', lang='{lang}'")
        print(f"[后端] 查询 '{query}' 命中 {len(results)} 条结果")

        return jsonify({"success": True, "data": results}) if results else jsonify({"success": False, "msg": "查无此词"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
