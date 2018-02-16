import os
import sqlite3

dir_path = os.path.dirname(os.path.realpath(__file__))
db_path = dir_path + '/database.db'


def get_lecturer_by_id(username):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("SELECT * FROM Lecturer WHERE username = ?;", [username])
    lecturer = {}
    for row in c:
        lecturer = {
            'username': row[0],
            'name': row[1],
            'password_hash': row[2]
        }

    conn.close()
    if not lecturer:
        raise ValueError("No lecturer found with username %s." % username)
    return lecturer
