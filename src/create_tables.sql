CREATE TABLE IF NOT EXISTS users(
    id          INTEGER PRIMARY KEY           ,
    username    TEXT    NOT NULL UNIQUE       ,
    password    TEXT    NOT NULL              ,
    is_admin    BOOLEAN NOT NULL DEFAULT False
);

CREATE TABLE IF NOT EXISTS messages(
    id          INTEGER PRIAMRY KEY          ,
    title       TEXT    NOT NULL             ,
    body        TEXT    NOT NULL             ,
    user_id     INTEGER NOT NULL             ,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO users(username, password, is_admin)
SELECT 'admin', 'admin', True
WHERE NOT EXISTS(SELECT 1 FROM users WHERE username == 'admin');
