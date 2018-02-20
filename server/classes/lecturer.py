import validation as valid
import hashlib


class Lecturer:
    def __init__(self, username, name, password_hash=None, password="password"):
        self.username = valid.username(username)
        self.name = valid.name(name)

        if password_hash:
            self.password_hash = password_hash
        else:
            self.password_hash = hashlib.sha512(password).hexdigest()(username)

    def dict(self):
        return vars(self)
