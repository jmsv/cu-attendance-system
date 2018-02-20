from flask import jsonify


class Response:
    def __init__(self, data, status=200):
        self.data = data
        self.status = status
        self.error = not 200 <= self.status < 300
        self.response_obj = None

    def send(self):
        self.response_obj = {
            'error': self.error,
            'data': self.data
        }

        return jsonify(self.response_obj), self.status
