from flask import Flask, request
import attending
import get_attendance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/attend")
def attend():
    student_id = request.args.get('user')
    event_uuid = request.args.get('event')
    return attending.attend(student_id,event_uuid)

@app.route("/placeholder")
def student_attendance():
    student_id = request.args.get('user')
    return get_attendance.attendance()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

