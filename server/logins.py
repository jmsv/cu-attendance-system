import sqlite3
import uuid
import hashlib
from datetime import datetime, timedelta
import database.logins_db as db
import validation

db_path = 'database/database.db'


def lecturer_login(username, password):
    lecturer = db.get_lecturer_by_id(username)
    password_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()
    if lecturer['password_hash'] != password_hash:
        raise ValueError("Wrong password")

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    session_key = uuid.uuid4().hex
    key_expires = datetime.now() + timedelta(days=1)
    key_expires_string = key_expires.strftime("%Y-%m-%d %H:%M:%S")

    c.execute("INSERT INTO LecturerLoginSessions VALUES(?, ?, ?);", [username, session_key, key_expires_string])

    conn.commit()
    conn.close()

    return session_key


def session_check(session_id):
    if not validation.session_id_is_valid(session_id):
        return False

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT lecturer_username, expires FROM LecturerLoginSessions WHERE session_id = ?;", (session_id,))
    result = c.fetchone()
    if not result:
        return False
    # TODO: If expiry datetime precedes current datetime, return False
    conn.close()
    return True
