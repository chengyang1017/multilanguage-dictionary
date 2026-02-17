-- 彻底删掉表
DROP TABLE IF EXISTS "mytable";

-- 重新建表
CREATE TABLE "mytable" (
  "word" TEXT NOT NULL PRIMARY KEY,
  "pos" TEXT NOT NULL,
  "translation" TEXT NOT NULL,
  "details" TEXT NOT NULL
);

DELETE FROM mytable;

INSERT INTO mytable(word, pos, translation, details) VALUES ('студент','名词(阳)','学生','单数：студент, студента, студенту, студента, студентом, о студенте; 复数：студенты, студентов, студентам, студентов, студентами, о студентах');
INSERT INTO mytable(word, pos, translation, details) VALUES ('книга','名词(阴)','书','单数：книга, книги, книге, книгу, книгой, о книге; 复数：книги, книг, книгам, книги, книгами, о книгах');
INSERT INTO mytable(word, pos, translation, details) VALUES ('окно','名词(中)','窗户','单数：окно, окна, окну, окно, окном, об окне; 复数：окна, окон, окнам, окна, окнами, об окнах');
INSERT INTO mytable(word, pos, translation, details) VALUES ('человек','名词(不规则)','人','单数：человек, человека, человеку, человека, человеком, о человеке; 复数：люди, людей, людям, людей, людьми, о людях');
INSERT INTO mytable(word, pos, translation, details) VALUES ('читать','动词(I)','读','现在时：читаю, читаешь, читает, читаем, читаете, читают; 过去时：читал, читала, читало, читали');
INSERT INTO mytable(word, pos, translation, details) VALUES ('говорить','动词(II)','说/讲','现在时：говорю, говоришь, говорит, говорим, говорите, говорят; 过去时：говорил, говорила, говорило, говорили');
INSERT INTO mytable(word, pos, translation, details) VALUES ('новый','形容词','新的','阳性：новый; 阴性：новая; 中性：новое; 复数：новые; 比较级：новее');
INSERT INTO mytable(word, pos, translation, details) VALUES ('хороший','形容词','好的','阳性：хороший; 阴性：хорошая; 中性：хорошее; 复数：хорошие; 比较级：лучше');
INSERT INTO mytable(word, pos, translation, details) VALUES ('идти','动词(变格特殊)','走/去','现在时：иду, идёшь, идёт, идём, идёте, идут; 过去时：шёл, шла, шло, шли');
INSERT INTO mytable(word, pos, translation, details) VALUES ('друг','名词(阳)','朋友','单数：друг, друга, другу, друга, другом, о друге; 复数：друзья, друзей, друзьям, друзей, друзьями, о друзьях');