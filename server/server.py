from flask import Flask, request, jsonify, render_template, send_from_directory

# Import other code files
import attending, get_attendance

app = Flask(__name__)


# Resource endpoints
# TODO: this should be made less hacky

# Javascript files
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)
# CSS files
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)


# Website index
@app.route('/')
def site_index():
    return render_template('index.html')


# API endpoints

# Test endpoint for checking server is working
@app.route('/api/hello')
def hello():
    return "hello"

# Endpoint called when student signs into their class
# TODO: Make this a POST method (not GET)
@app.route("/api/register-attendance")
def attend():
    student_id = request.args.get('user')
    event_uuid = request.args.get('event')
    return attending.attend(student_id,event_uuid)

# Get student's attendance history
@app.route("/api/student-attendance-history")
def student_attendance():
    student_id = request.args.get('user')
    return get_attendance.attendance()


# Run server for testing
if __name__ == "__main__":
    app.run()

