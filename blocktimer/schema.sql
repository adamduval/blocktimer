-- Store users in user table
-- Store timer in timer table
-- Store time blocks in time_block table
-- Initialize db and drop and existing databases

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS timer;
DROP TABLE IF EXISTS time_block;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE Not NULL,
    password TEXT NOT NULL
);

CREATE TABLE timer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    timer_name TEXT UNIQUE NOT NULL, 
    FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE time_block (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timer_id INTEGER NOT NULL,
    block TEXT NOT NULL,
    time INTEGER NOT NULL, 
    block_num INTEGER NOT NULL,
    FOREIGN KEY (timer_id) REFERENCES timer (id)
);
