/* Lecturer table data populated by code because passwords are hashed */

INSERT INTO Events (
                       lecturer_username,
                       datetime_end,
                       datetime_start,
                       room,
                       event_id
                   )
                   VALUES (
                       'dr777',
                       '2018-03-01 12:00:00',
                       '2018-03-01 10:00:00',
                       'ECG24',
                       'testc7474f4d1a26'
                   ),
                   (
                       'al010',
                       '2018-03-01 18:00:00',
                       '2018-03-01 16:00:00',
                       'ECG01',
                       'test9a65a035b5ca'
                   );

INSERT INTO Student (
                        username,
                        name,
                        sid
                    )
                    VALUES (
                        'torvalds',
                        'Linus Torvalds',
                        7080002
                    ),
                    (
                        'turing2',
                        'Alan Turing',
                        7080001
                    );

INSERT INTO Attendance (
                           event_id,
                           arrival,
                           sid
                       )
                       VALUES (
                           'test9a65a035b5ca',
                           '2018-03-01 16:04:17',
                           7080001
                       ),
                       (
                           'testc7474f4d1a26',
                           '2018-03-01 10:15:02',
                           7080001
                       );
