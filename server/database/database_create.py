import hashlib
import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
db_path = dir_path + '/database.db'


def drop_tables():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    drop_tables_sql = open(dir_path + "/sql/drop-tables.sql", "r")
    drops = drop_tables_sql.read().split('\n')
    drop_tables_sql.close()

    for drop in drops:
        try:
            c.execute(drop)
        except sqlite3.OperationalError as e:
            print("drop_tables:\t%s" % str(e))

    conn.commit()
    conn.close()


def create_tables():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    create_tables_sql = open(dir_path + "/sql/create-tables.sql", "r")
    creates = create_tables_sql.read().split('\n\n\n')
    create_tables_sql.close()

    for create in creates:
        try:
            c.execute(create)
        except sqlite3.OperationalError as e:
            print("create_tables:\t%s" % str(e))

    conn.commit()
    conn.close()


def init_lecturers():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    lecturers = [
        {
            'username': 'dr777',
            'name': 'Dennis Richie',
            'password': 'what lmao'
        }
    ]
    for l in lecturers:
        try:
            c.execute("INSERT INTO Lecturer VALUES (?, ?, ?);",
                      [l['username'], l['name'], hashlib.sha512(l['password'].encode('utf-8')).hexdigest()])
        except sqlite3.IntegrityError as e:
            print("init_lecturers:\t%s" % str(e))
    conn.commit()
    conn.close()


def get_usable_db():
    create_tables()
    init_lecturers()


def reset_db():
    drop_tables()
    get_usable_db()


if __name__ == '__main__':
    reset_db()
