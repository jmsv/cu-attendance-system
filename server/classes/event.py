import validation as valid


class Event:
    def __init__(self, event_id, room, start, end, lecturer):
        self.event_id = event_id
        self.room = room
        self.start = start
        self.end = end
        self.lecturer = valid.username(lecturer)

    def dict(self):
        return vars(self)
