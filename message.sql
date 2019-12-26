--
-- ��SQLiteStudio v3.1.1 �������ļ� ��һ 9�� 16 16:06:00 2019
--
-- �ı����룺System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- ��messages
DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    subject  TEXT    NOT NULL,
    sender   TEXT    NOT NULL,
    reply_to INT,
    text     TEXT    NOT NULL
);

INSERT INTO messages (id, subject, sender, reply_to, text) VALUES (1, 'subject test 1', 'tester 1', NULL, 'this is a test 1,aaaaaaaaaaaaaaaaaaalsscscssssssssssssssssssssssssssssssssssssssssssssss,dsdsfdasfafsa.safafafafafafafafafa');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
