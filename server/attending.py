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


def attendance(student_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM Attendance WHERE sid = '%s'" % student_id)
    attendance = []
    for row in c:
        cur = {}
        cur['sid'] = row[0]
        cur['arrival'] = row[1]
        cur['event_id'] = row[2]
        attendance.append(cur)
    conn.close
    print(attendance)
    return attendance
