CREATE TABLE Student(
StudentID NUMBER(7) NOT NULL PRIMARY KEY,
Name CHAR(30),
Username VARCHAR(15));

CREATE TABLE Lecturer(
LecturerID VARCHAR(8) NOT NULL PRIMARY KEY,
LecturerFirstName CHAR(15),
PasswordHash VARCHAR(16)

CREATE TABLE Events(
EventID VARCHAR(23) NOT NULL PRIMARY KEY,
Room VARCHAR(7),
Date DATE,
Start TIME,
Finished TIME,

CREATE TABLE Attendance(
StudentID NUMBER(7),
EntryTime TIME,
EventID VARCHAR(23));

ALTER TABLE Attendance(
ADD CONSTRAINT PK_Attendance PRIMARY KEY (StudentID, EventID));

^the above should make the tables
as for adding values to the tables

INSERT INTO Student VALUES (12345, 'Jon Doe', 'JDoe1')
INSERT INTO Student VALUES (13579, 'Alex Smith', 'ASmith1')
INSERT INTO Student VALUES (24682, 'Rose Joe', 'RJoe1')

INSERT INTO Lecturer VALUES (AB123456, 'Alexia Amazon', #(find out))
INSERT INTO Lecturer VALUES (AB654321, 'Siri Apple', #(find out))

INSERT INTO Events VALUES (*generated from code*, 'ECG-26', 02/02/2018, 14:00, 18:00)
INSERT INTO Events VALUES (*generated from code*, 'SHB-02', 02/02/2018, 09:00, 11:00)
INSERT INTO Events VALUES (*generated from code*, 'EC1-03', 03/02/2018, 15:00, 15:00)

as for the last one ill look at it tomorrow
