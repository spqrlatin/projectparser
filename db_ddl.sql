CREATE TABLE Users (
  id integer PRIMARY KEY AUTOINCREMENT,
  firstname varchar PRIMARY KEY AUTOINCREMENT,
  lastname varchar PRIMARY KEY AUTOINCREMENT,
  middlename varchar PRIMARY KEY AUTOINCREMENT,
  compensation varchar,
  experience integer,
  contacts varchar,
  ensurance_id integer,
  rso_id blob,
  url varchar
);

CREATE TABLE rsodata (
  id integer PRIMARY KEY AUTOINCREMENT,
  reestr_number integer,
  satisfied blob,
  excluded varchar,
  stopped varchar,
  grade varchar
);

CREATE TABLE ensurance (
  id integer PRIMARY KEY AUTOINCREMENT,
  ensurance_org varchar PRIMARY KEY AUTOINCREMENT
);