drop table if exists users;
CREATE TABLE users (
  user_id INTERGER PRIMARY KEY,
  email varchar(120) UNIQUE NOT NULL,
  user_name varchar(50) UNIQUE NOT NULL,
  admin SMALLINT NOT NULL DEFAULT 0,
  first_name VARCHAR(200) NOT NULL,
  last_name VARCHAR(200) NOT NULL,
  salt VARCHAR(64) NOT NULL,
  hash VARCHAR(64) NOT NULL
);

drop table if exists bks;
CREATE TABLE books (
  book_id int primary key,
  title varchar(200) NOT NULL,
  isbn_10 INTERGER,
  isbn_13 INTERGER,
  author_last_name varchar(50),
  author_first_name varchar(50),
  status int DEFAULT 0,
  synopsis VARCHAR(1000),
  image VARCHAR (100)
);
