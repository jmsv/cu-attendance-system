import datetime
import sqlite3
import uuid
import validation

db_path = 'database/database.db'


# attendance table functions


def register_student_attendance(student_id, event_uuid):
    try:
        student_id = validation.sid(student_id)
    except ValueError:
        return {
            'message': 'Invalid student ID'
        }, 400

    try:
        event_uuid = validation.event_id(event_uuid)
    except ValueError:
        return {
            'message': 'Invalid event ID'
        }, 400

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    arrival = datetime.datetime.now()
    arrival = arrival.strftime("%Y-%m-%d %H:%M:%S")
    try:
        c.execute("INSERT INTO Attendance VALUES(?, ?, ?);", [student_id, arrival, event_uuid])
    except sqlite3.IntegrityError:
        return {
            'message': 'Already signed in'
        }, 200

    conn.commit()
    conn.close()
    return {
        'message': 'Successfully signed in'
    }, 200


def get_student_attendance(student_id):
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


def get_attendance_for_event(event_uuid):
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


def get_events_by_lecturer(lecturer_username):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("SELECT * FROM Events WHERE lecturer_username = ?;", [lecturer_username])
    event_lecturer_list = []
    for row in c:
        cur = {
            'event_id': row[0],
            'room': row[1],
            'datetime_start': row[2],
            'datetime_end': row[3],
            'lecturer_username': row[4]
        }
        event_lecturer_list.append(cur)

    conn.close()
    return event_lecturer_list


def get_event(event_uuid):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("SELECT * FROM Events WHERE event_id = ?;", [event_uuid])
    row = c.fetchone()
    event = {
        'event_id': row[0],
        'room': row[1],
        'datetime_start': row[2],
        'datetime_end': row[3],
        'lecturer_username': row[4]
    }
    conn.close()
    return event


def create_event(room, start, end, lecturer):
    event_id = str(uuid.uuid4()).replace('-', '')[:16]

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    start_str = start.strftime("%Y-%m-%d %H:%M:%S")
    end_str = end.strftime("%Y-%m-%d %H:%M:%S")
    try:
        c.execute("INSERT INTO Events VALUES(?, ?, ?, ?, ?);",
                  [event_id, room, start_str, end_str, lecturer])
    except sqlite3.OperationalError:
        return False

    conn.commit()
    conn.close()

    return event_id

def student_was_late(event_id, arrival_time):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("SELECT * FROM Events WHERE event_id = ?;", [event_id])
    row = c.fetchone()
    start_time = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
    late_time = start_time + datetime.timedelta(minutes=15)
    arrival_time = datetime.datetime.strptime(arrival_time, "%Y-%m-%d %H:%M:%S")
    if arrival_time > late_time:
        return True
    return False





    
    
