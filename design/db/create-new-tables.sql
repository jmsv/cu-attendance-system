CREATE TABLE Student(
	sid INT NOT NULL PRIMARY KEY,
	name VARCHAR(64),
	username VARCHAR(16)
);

CREATE TABLE Lecturer(
	lecturer_id INT NOT NULL PRIMARY KEY,
	name VARCHAR(64),
	password_hash VARCHAR(64)
);

CREATE TABLE Events(
	event_id VARCHAR(16) NOT NULL PRIMARY KEY,
	room VARCHAR(8),
	datetime_start DATETIME,
	datetime_end DATETIME,
  	lecturer_id INT,

	FOREIGN KEY(lecturer_id) REFERENCES Lecturer(lecturer_id)
);

CREATE TABLE Attendance(
	sid INT NOT NULL,
	arrival_time DATETIME NOT NULL,
	event_id VARCHAR(16) NOT NULL,

	PRIMARY KEY (sid, event_id),

	FOREIGN KEY(event_id) REFERENCES Events(event_id),
	FOREIGN KEY(sid) REFERENCES Student(sid)
);

