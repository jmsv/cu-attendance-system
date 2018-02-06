from flask import Flask, request, jsonify, render_template, send_from_directory
import attending, get_attendance
app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)

@app.route('/')
def site_index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "hello"

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

