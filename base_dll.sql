DROP TABLE IF EXISTS cliente;

CREATE TABLE cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    lastname TEXT NOT NULL
);