import hashlib
import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
db_path = dir_path + '/database.db'

verbose = False


def v_print(text):
    if verbose:
        print(text)


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
            v_print("drop_tables:\t%s" % str(e))

    conn.commit()
    conn.close()


def create_tables():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    with open(dir_path + "/sql/create-tables.sql", "r") as file:
        sql = file.read()

    try:
        c.executescript(sql)
    except sqlite3.OperationalError as e:
        v_print("create_tables: " + str(e))

    conn.commit()
    conn.close()


def init_lecturers():
    lecturers = [
        ['dr777', 'Dennis Richie', 'what lmao'],
        ['al010', 'Ada Lovelace', 'program'],
    ]
    for l in lecturers:
        l[2] = hashlib.sha512(l[2].encode('utf-8')).hexdigest()

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    try:
        c.executemany("INSERT INTO Lecturer VALUES (?, ?, ?);", lecturers)
    except sqlite3.IntegrityError as e:
        v_print("init_lecturers:\t%s" % str(e))
    conn.commit()
    conn.close()


def example_data():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    with open(dir_path + "/sql/example-data.sql", "r") as file:
        sql = file.read()

    try:
        c.executescript(sql)
    except sqlite3.IntegrityError as e:
        v_print("example_data: " + str(e))

    conn.commit()
    conn.close()


def get_usable_db():
    create_tables()
    init_lecturers()
    example_data()


def reset_db():
    drop_tables()
    get_usable_db()


if __name__ == '__main__':
    reset_db()
