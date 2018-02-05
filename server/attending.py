import sqlite3

def attend(student_id,event_uuid):
    conn = sqlite3.connect('insertPathHere')
    c = conn.cursor()
    c.execute("INSERT INTO Attendance VALUES(?,?);",(student_id,event_uuid))
    conn.commit()
    conn.close()
    return "added"
