import os
import sqlite3

import validation as get_valid
from classes import *

dir_path = os.path.dirname(os.path.realpath(__file__))
db_path = dir_path + '/database.db'


def enc(string):
    return string.encode('ascii', 'ignore')


def get_student_by_id(sid):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    sid = get_valid.sid(sid)  # Will throw ValueError if invalid sid
    c.execute("SELECT * FROM Student WHERE sid = ?;", (sid,))
    result = c.fetchone()
    if not result:
        return None

    result_student = Student(sid, enc(result[1]), enc(result[2]))
    conn.close()
    return result_student


def get_lecturer_by_username(username):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM Lecturer WHERE username = ?;", (username,))
    result = c.fetchone()
    if not result:
        return None

    result_student = Lecturer(username, enc(result[1]), enc(result[2]))
    conn.close()
    return result_student
