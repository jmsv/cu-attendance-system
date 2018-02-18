from classes import *
import unittest


class TestStudents(unittest.TestCase):
    def test_title(self):
        s = Student(7234567, "pasta lasagne", "lasagne7")
        self.assertEqual(s.name, 'Pasta Lasagne')

    def test_str_sid(self):
        s = Student("1010101", "lmao", "lmao3")
        self.assertEqual(s.sid, 1010101)

    def test_dict(self):
        s = Student(7346348, "what", "what90")
        s_dict = {'name': 'What', 'sid': 7346348, 'username': 'what90'}
        self.assertEqual(s.dict(), s_dict)


class TestRooms(unittest.TestCase):
    def test_building(self):
        r = Room("ECG24")
        self.assertEqual(r.building, "Engineering & Computing Building")

    def test_unknown(self):
        r = Room("OOPS99")
        self.assertEqual(r.building, "Unknown building")

    def test_weird_room_code(self):
        r = Room("e cg - 24")
        self.assertEqual(r.code, "ECG24")
        self.assertEqual(r.building, "Engineering & Computing Building")


if __name__ == '__main__':
    unittest.main()
