from __future__ import print_function


def sid(value):
    """
    Get valid Student ID
    Must be a <=7 digit integer
    :param value: sid
    :return: valid sid
    """
    if not value: raise ValueError("sid (Student ID) not specified")

    if not isinstance(value, int):
        try:
            value = int(value)
        except ValueError:
            raise ValueError("sid (Student ID) must be an integer")

    if len(str(value)) > 7:
        raise ValueError("sid (Student ID) must be <=7 digits long")

    return value


def name(value):
    """
    Get valid name
    Must be a string
    :param value: name
    :return: valid name
    """
    if not isinstance(value, str):
        raise ValueError("Name must be an string")

    # Make first letter of each word uppercase
    value = value.title()

    return value


def username(value):
    """
    Get valid username
    Must be a string
    :param value: username
    :return: valid username
    """
    if not isinstance(value, str):
        try:
            value = value.encode('ascii', 'ignore')
        except:
            raise ValueError("Username must be a string, not %s" % type(value))

    return value


def room_code(value):
    """
    Get valid room code
    Must be a string, made up exclusively of uppercase letters and numbers
    :param value: room code
    :return: valid room code
    """
    if not isinstance(value, str):
        try:
            value = value.encode('ascii', 'ignore')
        except:
            raise ValueError("Room code must be a string, not %s" % type(value))

    # Make the value uppercase
    value = value.upper()

    allowed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    filtered = ''
    for char in value:
        if char in allowed:
            filtered += char
    value = filtered

    return value


def event_id(value):
    """
    Event ID must be 16 chars long, string
    :param value: event id
    :return: valid event id
    """
    value = str(value)
    if len(value) is not 16:
        raise ValueError("Event ID must be 16 characters long")
    return value


def session_id_is_valid(session_id):
    print(session_id)
    if not session_id:
        return False
    if len(session_id) != 32:
        return False
    return True
