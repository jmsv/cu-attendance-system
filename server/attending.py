import sqlite3

db_path = 'database.db'


def attend(student_id,arrival,event_uuid):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO Attendance VALUES(?,?,?);",(student_id,arrival,event_uuid))
    conn.commit()
    conn.close()
    return True


def attendance():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return {}
