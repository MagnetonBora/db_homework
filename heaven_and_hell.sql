CREATE TABLE IF NOT EXISTS courses (
  course_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR,
  ects INTEGER,
  price decimal,
  start_date DATE,
  end_date DATE,
  type VARCHAR
);

CREATE TABLE IF NOT EXISTS online_course (
  course_id INTEGER PRIMARY KEY AUTOINCREMENT,
  url VARCHAR
);

CREATE TABLE IF NOT EXISTS onsite_course (
  course_id INTEGER primary key AUTOINCREMENT,
  address VARCHAR,
  duartion INTEGER
);

CREATE TABLE IF NOT EXISTS departement (
  departement_id INTEGER PRIMARY KEY AUTOINCREMENT,
  departement_name VARCHAR,
  address VARCHAR,
  manager VARCHAR,
  budget INTEGER
);

CREATE TABLE IF NOT EXISTS employees (
  employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR,
  last_name VARCHAR,
  start_date DATE,
  PESEL INTEGER,
  telephone INTEGER,
  address VARCHAR
);

CREATE TABLE IF NOT EXISTS student_grades (
  student_id INTEGER,
  course_id INTEGER,
  ects INTEGER,
  grade INTEGER
);

CREATE TABLE IF NOT EXISTS students (
  student_id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR,
  last_name VARCHAR,
  address VARCHAR,
  PESEL INTEGER,
  telephone INTEGER
);
