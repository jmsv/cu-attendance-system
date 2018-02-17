import validation as valid


class Student:
    def __init__(self, sid, name, username):
        self.sid = valid.sid(sid)
        self.name = valid.name(name)
        self.username = valid.username(username)

    def dict(self):
        return vars(self)
