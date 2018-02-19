import validation as valid

buildings = (
    ["AB", "Alan Berry", ()],
    ["AS", "Armstrong Siddely", ()],
    ["CUSC", "Coventry University Sports Centre", ()],
    ["CW", "Charles Ward", ()],
    ["EC", "Engineering & Computing Building", ("52.405219", "-1.499655")],
    ["ET", "Ellen Terry", ()],
    ["FL", "Frederick Lanchester Library", ()],
    ["GE", "George Eliot", ()],
    ["GS", "Graham Sutherland", ()],
    ["HUB", "The Hub", ()],
    ["JA", "Jaguar", ()],
    ["JL", "John Laing", ()],
    ["JS", "James Starley", ()],
    ["MF", "Maurice Foss", ()],
    ["RC", "Richard Crossman", ()],
    ["SC", "Student Centre", ()],
    ["SHB", "Science & Health Building", ()],
    ["WM", "William Morris", ()],
)


class Room:
    def __init__(self, room_code, building=None):
        self.code = valid.room_code(room_code)
        self.building = building
        self.coordinates = ()

        if not self.building:
            self.building = "Unknown building"
            self.__get_room_details()

    def __get_room_details(self):
        for building in buildings:
            if self.code.find(building[0]) == 0:
                self.building = building[1]
                self.coordinates = building[2]
                return
