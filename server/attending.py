import sqlite3

db_path = 'database.db'


def attend(student_id,event_uuid):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # TODO: Insert needs `arrival` param
    c.execute("INSERT INTO Attendance VALUES(?,?);",(student_id,event_uuid))
    conn.commit()
    conn.close()
    return True


def attendance():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    return {}
