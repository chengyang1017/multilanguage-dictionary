from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import json

app = Flask(__name__)
DB_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'databases')

def get_db_connection(lang):
    db_path = os.path.join(DB_FOLDER, f'{lang}.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    lang = request.args.get('lang', 'ru').lower()
    
    if not query: return jsonify({"success": False, "msg": "请输入内容"})

    table = f"{lang}_table"
    try:
        conn = get_db_connection(lang)
        cursor = conn.cursor()
        
        # 终极查询语句：指定表名避免歧义，联表查询 JSON 每一个值
        sql = f"""
            SELECT DISTINCT {table}.* FROM {table}, json_each({table}.data)
            WHERE {table}.word LIKE ? 
            OR {table}.meanings LIKE ? 
            OR json_each.value LIKE ?
        """

        # 构造参数：全部使用模糊匹配提高容错率
        search_param = f"%{query}%"
        cursor.execute(sql, (search_param, search_param, search_param))
        rows = cursor.fetchall()

        results = []
        for row in rows:
            # 增加一个容错：检查 data 到底是不是字符串
            raw_data = row["data"]
            details = json.loads(raw_data) if isinstance(raw_data, str) else raw_data

            results.append({
                "headword": row["word"],
                "meanings": row["meanings"], # 改名
                "type": row["type"],
                "all_details": details
            })

        return jsonify({"success": True, "data": results}) if results else jsonify({"success": False, "msg": "查无此词"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)