import validation as valid

buildings = (
    ["AB", "Alan Berry", ("52.408037", "-1.5057018")],
    ["AS", "Armstrong Siddely", ("52.407593", "-1.501042")],
    ["CUSC", "Coventry University Sports Centre", ("52.4057853", "-1.5042181")],
    ["CW", "Charles Ward", ("52.408542", "-1.505167")],
    ["EC", "Engineering & Computing Building", ("52.405219", "-1.499655")],
    ["ET", "Ellen Terry", ("52.4066632", "-1.5046563")],
    ["FL", "Frederick Lanchester Library", ("52.4060817", "-1.5005275")],
    ["GE", "George Eliot", ("52.4079898", "-1.5047571")],
    ["GS", "Graham Sutherland", ("52.4070953", "-1.5030317")],
    ["HUB", "The Hub", ("52.4074963", "-1.5047307")],
    ["JA", "Jaguar", ("52.4070482", "-1.5010405")],
    ["JL", "John Laing", ("52.4058614", "-1.5049971")],
    ["JS", "James Starley", ("52.4077121", "-1.5040618")],
    ["MF", "Maurice Foss", ("52.4078156", "-1.5031266")],
    ["RC", "Richard Crossman", ("52.4066513", "-1.5051487")],
    ["SC", "Student Centre", ("52.404955", "-1.50074")],
    ["SHB", "Science & Health Building", ("52.4053983", "-1.5040591")],
    ["WM", "William Morris", ("52.406556", "-1.5011871")],
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
