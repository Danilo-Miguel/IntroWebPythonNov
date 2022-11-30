DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
    id integer primary key autoincrement,
    titulo string not null, 
    texto string not null,
    data_criacao TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
);