from flask import Flask, request, jsonify, render_template, send_from_directory

# Import other code files
import attending

app = Flask(__name__, template_folder='static', static_folder='static')


# Website index
@app.route('/')
def site_index():
    return render_template('index.html')


# Assets
@app.route('/static/<path:path>')
def get_assets(path):
    return send_from_directory(app.static_folder, path)


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
    return attending.attend(student_id, event_uuid)


# Get student's attendance history
@app.route("/api/student-attendance-history")
def student_attendance():
    student_id = request.args.get('user')
    return jsonify(attending.attendance(student_id))


# Run server for testing
if __name__ == "__main__":
    app.run()
