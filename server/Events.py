import sqlite3

db_path = '.db'

def event_lecturer(lecturer_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM Events WHERE lecturer_id = ?;", [lecturer_id])
    event_lecturer_list = []
    for row in c:
        cur = {
            'Event_id': row[0],
            'Room': row[1],
            'Date': row[2],
            'Start': row[3],
            'Finish': row[4]
            #add lecturer_id
        }
        event_lecturer_list.append(cur)
    conn.close()
    return event_lecturer_list
