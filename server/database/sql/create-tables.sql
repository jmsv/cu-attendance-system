CREATE TABLE Student(
  sid INT NOT NULL PRIMARY KEY,
  name VARCHAR(64),
  username VARCHAR(16)
);


CREATE TABLE Lecturer(
  username VARCHAR(16) NOT NULL PRIMARY KEY,
  name VARCHAR(64),
  password_hash VARCHAR(128)
);


CREATE TABLE Events(
  event_id VARCHAR(16) NOT NULL PRIMARY KEY,
  room VARCHAR(8),
  datetime_start DATETIME,
  datetime_end DATETIME,
  lecturer_username INT,
  FOREIGN KEY(lecturer_username) REFERENCES Lecturer(username)
);


CREATE TABLE Attendance(
  sid INT NOT NULL,
  arrival DATETIME NOT NULL,
  event_id VARCHAR(16) NOT NULL,
  PRIMARY KEY (sid, event_id),
  FOREIGN KEY(event_id) REFERENCES Events(event_id),
  FOREIGN KEY(sid) REFERENCES Student(sid)
);


CREATE TABLE LecturerLoginSessions(
  lecturer_username INT NOT NULL,
  session_id VARCHAR(32) NOT NULL,
  expires DATETIME NOT NULL,
  FOREIGN KEY(lecturer_username) REFERENCES Lecturer(username)
);


CREATE TABLE StudentLoginSessions(
  sid INT NOT NULL,
  session_id VARCHAR(32) NOT NULL,
  expires DATETIME NOT NULL,
  FOREIGN KEY(sid) REFERENCES Student(sid)
);