import sqlite3
import datetime

db_path = 'database.db'


def attend(student_id,event_uuid):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    arrival = datetime.datetime.now()
    arrival = arrival.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO Attendance VALUES(?,?,?);",(student_id,arrival,event_uuid))
    conn.commit()
    conn.close()
    return True


def attendance():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return {}
