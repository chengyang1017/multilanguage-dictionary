-- 以俄语为例：ru_table
CREATE TABLE IF NOT EXISTS ru_table (
    word TEXT PRIMARY KEY,   -- 存储“主词”（主格或不定式）
    root TEXT,              -- 存储中文意思（词根）
    type TEXT,              -- 标识：'名词', '动词', '形容词' 等
    data JSON               -- 存储所有的变格、变位、例句、体对
);

-- 索引必须加，否则 1000 种语言搜起来会卡
CREATE INDEX idx_ru_root ON ru_table(root);

-- 插入名词示例
INSERT OR REPLACE INTO ru_table (word, root, type, data) VALUES 
('определение', '定义', '名词', '{"主格": {"form": "определе́ние", "example": "..."}}');

-- 插入动词示例
INSERT OR REPLACE INTO ru_table (word, root, type, data) VALUES 
('есть', '吃', '动词', '{"完成体": "съесть", "现在时": {"я": "ем", "ты": "ешь", "он": "ест"}}');