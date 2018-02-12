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
  arrival DATETIME NOT NULL,
  event_id VARCHAR(16) NOT NULL,

  PRIMARY KEY (sid, event_id),

  FOREIGN KEY(event_id) REFERENCES Events(event_id),
  FOREIGN KEY(sid) REFERENCES Student(sid)
);


/* Data examples */

INSERT INTO Attendance VALUES (7085352, '2018-02-07 09:04:22', '31bf1addd9914e49');
INSERT INTO Attendance VALUES (6995666, '2007-01-01 09:01:59', '31bf1addd9914e49');
INSERT INTO Attendance VALUES (7011184, '2007-01-01 09:19:01', '31bf1addd9914e49');
INSERT INTO Attendance VALUES (7085352, '2007-01-01 11:32:15', 'f84ce22d07f54e18');
INSERT INTO Attendance VALUES (7000001, '2007-01-01 11:02:46', 'f84ce22d07f54e18');

