-- 1. 彻底删掉旧表（为了重新定义干净的结构）
DROP TABLE IF EXISTS "mytable";

-- 2. 重新建表，加入 lang_code 字段
CREATE TABLE "mytable" (
  "word" TEXT NOT NULL,
  "lang_code" TEXT NOT NULL,  -- 核心字段：'ru', 'tr', 'fr' 等
  "pos" TEXT NOT NULL,
  "translation" TEXT NOT NULL,
  "details" TEXT NOT NULL,
  PRIMARY KEY ("word", "lang_code") -- 联合主键：允许不同语言有相同的单词
);

-- 3. 插入测试数据时带上语言标识
INSERT INTO mytable VALUES ('студент', 'ru', '名词(阳)', '学生', '俄语变格详情...');
INSERT INTO mytable VALUES ('öğrenci', 'tr', '名词', '学生', '土耳其语变格详情...');
INSERT INTO mytable VALUES ('chat', 'fr', '名词(阳)', '猫', '法语变位/复数...');