from flask import Flask, request, jsonify, render_template, send_from_directory

import attending
import logins
import validation
import database.database_create as db

db.get_usable_db()

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


# Lecturer webapp
@app.route('/lecturer-webapp')
def site_lecturer_webapp():
    return render_template('lecturer-webapp.html')


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
    if not student_id or not event_uuid:
        return jsonify({'error' : 'ValueError: SID or Event_id not found'}),400
    return jsonify({'ok': attending.register_student_attendance(student_id, event_uuid)})


# Get student's attendance history
@app.route('/api/student-attendance-history', methods=['GET'])
def student_attendance():
    student_id = request.args.get('user')
    if not student_id:
        return jsonify({'error' : 'ValueError: SID not found'}),400
    return jsonify(attending.get_student_attendance(student_id))


# Get event's attendance history
@app.route('/api/event-attendance-history', methods=['GET'])
def event_attendance():
    event_uuid = request.args.get('event')
    if not event_uuid:
        return jsonify({'error' : 'ValueError: Event not found'}),400
    return jsonify(attending.get_attendance_for_event(event_uuid))

# Get lecturer's event history
@app.route('/api/lecturer-event-history', methods=['GET'])
def lecturer_events():
    lecturer_username = request.args.get('lecturer')
    if not lecturer_username:
        return jsonify({'error' : 'ValueError: Lecturer not found'}),400
    return jsonify(attending.get_events_by_lecturer(lecturer_username))

# Get event's details
@app.route('/api/event-details', methods=['GET'])
def event_details():
    event_id = request.args.get('lecturer')
    if not event_id:
        return jsonify({'error' : 'ValueError: Event not found'}),400
    return jsonify(attending.get_event(event_id))


# Lecturer login
@app.route('/api/lecturer-login', methods=['POST'])
def lecturer_login():
    username = request.form['username']
    password = request.form['password']
    try:
        key = logins.lecturer_login(username, password)
    except ValueError:
        return jsonify({'Error': 'Password incorrect'}, 403)
    except Exception as e:
        print e
        return jsonify({'Error': 'Internal Server Error'}, 500)
    return key


# Run server for testing
if __name__ == "__main__":
    app.config.update(
        DEBUG=True,
        TEMPLATES_AUTO_RELOAD=True
    )
    app.run()
