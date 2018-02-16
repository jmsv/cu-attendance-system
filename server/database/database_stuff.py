import logging
import os
import sqlite3

logging.basicConfig(filename='cuas-server.log', level=logging.DEBUG)

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
            logging.info("drop_tables:\t%s" % str(e))

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
            logging.info("create_tables:\t%s" % str(e))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    drop_tables()
    create_tables()
