import datetime
import sqlite3

db_path = 'database.db'

#attendance table functions

def attend(student_id, event_uuid):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    arrival = datetime.datetime.now()
    arrival = arrival.strftime("%Y-%m-%d %H:%M:%S")
    try:
        c.execute("INSERT INTO Attendance VALUES(?, ?, ?);", [student_id, arrival, event_uuid])
    except:
        return False
    conn.commit()
    conn.close()
    return True


def attendance(student_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM Attendance WHERE sid = ?;", [student_id])
    attendance_list = []
    for row in c:
        cur = {
            'sid': row[0],
            'arrival': row[1],
            'event_id': row[2]
        }
        attendance_list.append(cur)
    conn.close()
    return attendance_list


def event_attendance(event_uuid):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM Attendance WHERE event_id = ?;", [event_uuid])
    event_attendance_list = []
    for row in c:
        cur = {
            'sid': row[0],
            'arrival': row[1],
            'event_id': row[2]
        }
        event_attendance_list.append(cur)
    conn.close()
    return event_attendance_list

#events table functions

def event_lecturer(lecturer_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM Events WHERE lecturer_id = ?;", [lecturer_id])
    event_lecturer_list = []
    for row in c:
        cur = {
            'event_id': row[0],
            'room': row[1],
            'datetime_start': row[2],
            'datetime_end': row[3]
            'lecturer_id': row[4]
        }
        event_lecturer_list.append(cur)
    conn.close()
    return event_lecturer_list

