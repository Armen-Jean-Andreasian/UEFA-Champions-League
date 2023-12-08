from players.player import Player


class Midfielder(Player):
    def __init__(self, name, nationality, club, dob, position):
        super().__init__(name=name, nationality=nationality, club=club, date_of_birth=dob, position=position)

    def __str__(self):
        return super().__str__()


class DefenciveMidfielder(Midfielder):
    def __init__(self, name, nationality, club, dob):
        position = "DMF"
        super().__init__(name, nationality, club, dob, position)


class LeftMidfielder(Midfielder):
    def __init__(self, name, nationality, club, dob):
        position = "LM"
        super().__init__(name, nationality, club, dob, position)


class RightMidfielder(Midfielder):
    def __init__(self, name, nationality, club, dob):
        position = "RM"
        super().__init__(name, nationality, club, dob, position)


class CentralMidfielder(Midfielder):
    def __init__(self, name, nationality, club, dob):
        position = "CAM"
        super().__init__(name, nationality, club, dob, position)


class CentralAttackingMidfielder(Midfielder):
    def __init__(self, name, nationality, club, dob):
        position = "CAM"
        super().__init__(name, nationality, club, dob, position)


if __name__ == '__main__':
    d = CentralAttackingMidfielder(
        name="Modric",
        nationality="Croatia",
        club="Real Madrid",
        dob=""
    )
    print(d)
