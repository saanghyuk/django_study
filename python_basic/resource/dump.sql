BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'SON','sh@naver.com','010-3030-2030','kormat.co.kr','2021-02-10 16:44:34');
INSERT INTO "users" VALUES(2,'Yoon','syoon@gmail.com','010-6391-4103','Yoon.com','2021-02-10 16:44:34');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-3213-5325','Lee.com','2021-02-10 16:38:17');
INSERT INTO "users" VALUES(4,'LinXI
','xi@naver.com','010-1234-1234','linxi.com','2021-02-10 16:38:17');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-3213-5325','Yoo.com','2021-02-10 16:38:17');
COMMIT;
