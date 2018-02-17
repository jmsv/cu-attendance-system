def check_valid_sid(student_id):
    if len(student_id) != 7:
        return {'error' : 'ValueError: SID wrong length'},411

def check_valid_event_uuid(event_id):
    if len(event_id) != 16:
        return {'error' : 'ValueError: Event_id wrong length'},411
