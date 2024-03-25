CREATE TABLE IF NOT EXISTS Student (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	nickname TEXT
) STRICT;

CREATE TABLE IF NOT EXISTS Class (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
) STRICT;

CREATE TABLE IF NOT EXISTS Academy (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL
) STRICT;

 /* 
INSERT INTO Academy (name) VALUES ('FRA');

INSERT INTO Class (name) VALUES ('SPION21');

INSERT INTO Student  (first_name, last_name, nickname) VALUES ('Xi','Som', 'XS');

INSERT INTO Student  (first_name, last_name) VALUES ('Zorro','Vendetta');
 /* 