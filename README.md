# Multilanguage Dictionary

> A Chinese-centric multilingual dictionary for exploring vocabulary across 100+ languages.

**Multilanguage Dictionary** 是一个以中文为核心的多语言词典项目，目标是建立一个能够长期保存、整理和查询世界各语言词汇的数据系统。

项目使用 **Flask + SQLite** 提供查询服务，前端使用原生 **HTML / CSS / JavaScript** 构建。不同语言可以拥有独立的词库结构，并通过 Schema 描述不同语言、不同词性的字段。

除了词典查询功能之外，项目还提供了一套从 **Excel 原始词库 → SQLite 数据库** 的数据处理流程，方便持续扩充新的语言与词汇。

---

## Features

* 🌍 面向 100+ 种语言的多语言词典架构
* 🇨🇳 以中文作为主要释义与检索语言
* 🔎 支持中文和目标语言词汇搜索
* 🗂️ 每种语言使用独立 SQLite 数据库
* 🧩 不同语言可以定义独立的词条 Schema
* 📚 支持名词、动词、形容词等不同词性结构
* 📊 使用 Excel 管理原始词库数据
* 🔄 支持 Excel 自动转换为 SQLite
* 🎯 支持单独更新指定语言数据库
* 💻 响应式 Web 界面
* 🧱 搜索结果根据语言 Schema 动态生成

---

## Project Philosophy

很多主流词典只覆盖少数大型语言。

Multilanguage Dictionary 希望采用另一种思路：

**让大型语言、小型语言以及资料较少的语言，都能够拥有结构化保存词汇的空间。**

这个项目不仅仅是一个查询页面，也是在尝试建立一套可以不断扩展的多语言词汇数据体系。

核心关系可以理解为：

```text
Chinese
   │
   ├── English
   ├── Russian
   ├── Vietnamese
   ├── Uyghur
   ├── Indonesian
   ├── ...
   │
   └── More languages
```

不同语言不必强行共享完全相同的数据结构。

例如：

```text
Russian
├── gender
├── case
├── aspect
└── conjugation

Vietnamese
├── classifier
├── pronunciation
└── usage

English
├── plural
├── tense
└── comparative
```

这些差异通过语言 Schema 描述，并由前端动态展示。

---

## Architecture

```text
Excel Dictionary Data
        │
        ▼
   Python Scripts
        │
        ▼
      SQLite
        │
        ▼
      Flask
        │
        ▼
   /search API
        │
        ▼
HTML / CSS / JavaScript
        │
        ▼
 Dictionary Interface
```

### Backend

后端使用 Flask。

主要负责：

* 提供词典主页
* 接收搜索请求
* 根据语言加载对应 SQLite 数据库
* 查询不同词性对应的数据表
* 将词条数据转换为 JSON
* 返回给前端进行展示

搜索接口：

```text
GET /search
```

参数：

```text
query = 搜索内容
lang  = 目标语言代码
```

例如：

```text
/search?query=房子&lang=ru
```

---

## Dictionary Data

每种语言拥有独立的数据库：

```text
data/
├── raw_data/
│   ├── en_words.xlsx
│   ├── ru_words.xlsx
│   ├── vi_words.xlsx
│   └── ...
│
└── db/
    ├── en.db
    ├── ru.db
    ├── vi.db
    └── ...
```

Excel 文件作为主要的原始词库数据来源。

数据库则作为 Web 应用实际查询的数据源。

---

## Database Structure

每种语言可以根据词性建立多个数据表。

例如：

```text
ru_noun_table
ru_verb_table
ru_adjective_table
```

基本字段：

```text
word
meanings
type
data
```

其中：

* `word`：目标语言词汇
* `meanings`：中文释义
* `type`：词性
* `data`：完整词条信息，以 JSON 保存

这种设计允许不同语言保存不同的语法信息，而不需要强迫所有语言使用完全相同的数据库字段。

---

## Language Schema

语言词条的显示结构由：

```text
static/js/lang-schemas.js
```

定义。

Schema 可以指定：

* 某种语言有哪些词性
* 每种词性包含哪些字段
* 字段属于哪个展示区域
* 前端应该如何组织词条信息

前端读取 Schema 后动态生成词条卡片。

因此增加新的语言时，不需要为每种语言重新制作一套页面。

---

## Project Structure

```text
multilanguage-dictionary/
│
├── app.py
│   └── Flask 应用与词典搜索 API
│
├── templates/
│   └── index.html
│       └── 词典 Web 界面
│
├── static/
│   ├── js/
│   │   └── lang-schemas.js
│   └── ...
│
├── data/
│   ├── raw_data/
│   │   └── *_words.xlsx
│   │
│   └── db/
│       └── *.db
│
├── excel_to_db.py
│   └── Excel → SQLite 数据转换
│
├── update.py
│   └── 更新全部或指定语言数据库
│
├── convert_js_to_json.py
│   └── Schema 转换工具
│
├── force_init.py
│   └── 数据初始化工具
│
└── README.md
```

---

## Getting Started

### 1. Clone

```bash
git clone https://github.com/chengyang1017/multilanguage-dictionary.git
cd multilanguage-dictionary
```

### 2. Install dependencies

建议使用 Python 虚拟环境：

```bash
python -m venv .venv
```

Windows：

```bash
.venv\Scripts\activate
```

安装主要依赖：

```bash
pip install flask pandas openpyxl
```

SQLite 由 Python 标准库提供，不需要额外安装 Python 包。

---

## Run the Dictionary

启动 Flask：

```bash
python app.py
```

然后在浏览器打开 Flask 输出的本地地址。

默认开发环境通常为：

```text
http://127.0.0.1:5000
```

进入页面后：

1. 选择目标语言
2. 输入中文或目标语言词汇
3. 提交搜索
4. 查看结构化词条信息

---

## Update Dictionary Data

### Update all languages

将 Excel 数据重新生成到 SQLite：

```bash
python update.py
```

程序会检查语言 Schema，并处理已经存在对应 Excel 数据的语言。

---

### Update one language

只更新指定语言：

```bash
python update.py --lang ru
```

例如：

```bash
python update.py --lang en
python update.py --lang vi
```

这样在修改单个语言的大型词库时，不需要重新生成所有数据库。

---

## Adding a New Language

新增语言的大致流程：

```text
1. 创建语言 Excel 词库
        ↓
2. 配置语言 Schema
        ↓
3. 运行 update.py
        ↓
4. 生成语言 SQLite 数据库
        ↓
5. 前端选择该语言
        ↓
6. 开始查询
```

例如增加语言代码：

```text
xx
```

创建：

```text
data/raw_data/xx_words.xlsx
```

然后在：

```text
static/js/lang-schemas.js
```

加入对应语言的词条结构。

最后执行：

```bash
python update.py --lang xx
```

即可生成：

```text
data/db/xx.db
```

---

## Search Flow

一次搜索的大致过程：

```text
用户输入
   │
   ▼
选择目标语言
   │
   ▼
GET /search
   │
   ▼
Flask
   │
   ▼
加载对应语言 SQLite
   │
   ▼
搜索 word / meanings / data
   │
   ▼
返回 JSON
   │
   ▼
根据 LANG_SCHEMAS 渲染
   │
   ▼
显示词条
```

---

## Tech Stack

### Backend

* Python
* Flask
* SQLite
* Pandas

### Frontend

* HTML
* CSS
* JavaScript

### Dictionary Pipeline

* Excel
* Python
* JSON
* SQLite

---

## Roadmap

这个项目仍在持续扩展。

计划方向包括：

* [ ] 增加更多语言
* [ ] 持续扩充现有语言词库
* [ ] 完善语言与词性 Schema
* [ ] 改进搜索算法
* [ ] 增加模糊搜索
* [ ] 增加词形变化搜索
* [ ] 增加语言别名与语言代码管理
* [ ] 优化大型词库查询性能
* [ ] 完善移动端体验
* [ ] 建立更加统一的多语言词汇数据规范

---

## Goal

这个项目的长期目标并不是只制作几个常见语言的词典。

而是建立一个能够不断扩展的：

**Multilingual Lexical Database**

让尽可能多的语言拥有结构化、可查询、可长期保存的词汇资料。

> One dictionary architecture, many languages.

---

## Author

**Cheng Yang**

Multilanguage Dictionary is an experimental multilingual dictionary and lexical data project focused on building a scalable structure for languages around the world.
