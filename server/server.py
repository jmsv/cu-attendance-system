from flask import Flask, request, jsonify, render_template, send_from_directory

# Import other code files
import attending
import database.database_stuff as db

db.create_tables()

app = Flask(__name__, template_folder='static', static_folder='static')


# Website index
@app.route('/')
def site_index():
    return render_template('index.html')


# Splash screen
@app.route('/splash')
def site_splash():
    return render_template('splash.html')


# Lecturer login
@app.route('/lecturer-login')
def site_lecturer_login():
    return render_template('lecturer-login.html')


# Assets
@app.route('/static/<path:path>')
def get_assets(path):
    return send_from_directory(app.static_folder, path)


# Test endpoint for checking server is working
@app.route('/api/hello')
def hello():
    return "hello"


# Endpoint called when student signs into their class
@app.route('/api/register-attendance', methods=['POST'])
def attend():
    student_id = request.form['user']
    event_uuid = request.form['event']
    # TODO: If either of the above values aren't present in the request, return 400
    return jsonify({'ok': attending.attend(student_id, event_uuid)})


# Get student's attendance history
@app.route('/api/student-attendance-history', methods=['GET'])
def student_attendance():
    student_id = request.args.get('user')
    return jsonify(attending.attendance(student_id))


# Get event's attendance history
@app.route('/api/event-attendance-history', methods=['GET'])
def event_attendance():
    event_uuid = str(request.args.get('event'))
    return jsonify(attending.event_attendance(event_uuid))


# Run server for testing
if __name__ == "__main__":
    app.config.update(
        DEBUG=True,
        TEMPLATES_AUTO_RELOAD=True
    )
    app.run()
