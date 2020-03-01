from sqlalchemy import create_engine


def create_db(engine, queries):
    for query in queries:
        execute_query(engine, query)


def execute_query(engine, query):
    return engine.execute(query)


def select_all(table, engine):
    return engine.execute(f'select * from {table}'). fetchall()


if __name__ == '__main__':
    url = 'sqlite:///:memory:'
    engine = create_engine(url)

queries = [
    'CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY AUTOINCREMENT, \n'
    'title VARCHAR, ects INTEGER, \n'
    'price decimal, \n'
    'start_date DATE,\n '
    'end_date DATE, \n'
    'type VARCHAR);',

    'CREATE TABLE IF NOT EXISTS online_course (course_id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
    'url VARCHAR);',

    'CREATE TABLE IF NOT EXISTS onsite_course (course_id INTEGER primary key AUTOINCREMENT,\n'
    'address VARCHAR, duartion INTEGER);',

    'CREATE TABLE IF NOT EXISTS departement (departement_id INTEGER PRIMARY KEY AUTOINCREMENT, \n'
    'departement_name VARCHAR, \n'
    'address VARCHAR, \n'
    'manager VARCHAR, \n'
    'budget INTEGER);',

    'CREATE TABLE IF NOT EXISTS employees (employee_id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
    'first_name VARCHAR, \n'
    'last_name VARCHAR, \n'
    'start_date DATE, \n'
    'PESEL INTEGER, \n'
    'telephone INTEGER, \n'
    'address VARCHAR);',

    'CREATE TABLE IF NOT EXISTS stuent_grades (student_id INTEGER, \n'
    'course_id INTEGER,\n'
    'ects INTEGER,\n'
    'grade INTEGER);',

    'CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY AUTOINCREMENT, \n'
    'first_name VARCHAR,\n'
    'last_name VARCHAR, \n'
    'address VARCHAR, \n'
    'pesel INTEGER, \n'
    'telephone INTEGER);'
]

table = ['INSERT INTO courses (title) VALUES ("Basic Excel")',
         'INSERT INTO courses (price) VALUES (350)',
         'INSERT INTO courses (start_date) VALUES (23-01-2020)',
         'INSERT INTO courses (end_date) VALUES (25-01-2020)',
         'INSERT INTO courses (type) VALUES ("onsite")',
         ]

create_db(engine, queries)
create_db(engine, table)
