import os
import re
import json

# -----------------------------
# 路径设置
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JS_FILE = os.path.join(BASE_DIR, "static/js/lang-schemas.js")
JSON_FILE = os.path.join(BASE_DIR, "static/js/lang-schemas.json")

# -----------------------------
# 读取 JS 文件
# -----------------------------
with open(JS_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# -----------------------------
# 清理 JS 语法，生成合法 JSON
# -----------------------------

# 1️⃣ 去掉开头 const LANG_SCHEMAS =
text = re.sub(r"^const\s+LANG_SCHEMAS\s*=\s*", "", text.strip(), flags=re.M)

# 2️⃣ 去掉末尾分号
text = re.sub(r";\s*$", "", text)

# 3️⃣ 去掉所有 // 注释
text = re.sub(r"//.*", "", text)

# 4️⃣ 用正则把单引号改成双引号（仅键名和字符串值）
# 注意这里假设 JS 里只有单引号用于键和值，复杂表达式可能需要手动修
text = re.sub(r"'([^']*)'", r'"\1"', text)

# 5️⃣ 移除多余逗号（可选，根据你的文件）
text = re.sub(r",(\s*[\]}])", r"\1", text)

# -----------------------------
# 转成 JSON 对象，检查是否合法
# -----------------------------
try:
    data = json.loads(text)
except json.JSONDecodeError as e:
    print("❌ JSON 解析失败:", e)
    exit(1)

# -----------------------------
# 写入 JSON 文件
# -----------------------------
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"✅ 成功生成 JSON 文件: {JSON_FILE}")
