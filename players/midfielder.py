from players.player import Player


class Midfielder(Player):
    def __init__(self, name, national_team_obj, club, dob, position):
        super().__init__(name=name, national_team_obj=national_team_obj, position=position, club_obj=club,
                         date_of_birth=dob)

    def __str__(self):
        return super().__str__()


class DefenciveMidfielder(Midfielder):
    position = "DMF"

    def __init__(self, name, national_team_obj, club, dob):
        super().__init__(name, national_team_obj, club, dob, self.position)


class LeftMidfielder(Midfielder):
    position = "LM"

    def __init__(self, name, national_team_obj, club, dob):
        super().__init__(name, national_team_obj, club, dob, self.position)


class RightMidfielder(Midfielder):
    position = "RM"

    def __init__(self, name, national_team_obj, club, dob):
        super().__init__(name, national_team_obj, club, dob, self.position)


class CentralMidfielder(Midfielder):
    position = "CM"

    def __init__(self, name, national_team_obj, club, dob):
        super().__init__(name, national_team_obj, club, dob, self.position)


class CentralAttackingMidfielder(Midfielder):
    position = "CAM"

    def __init__(self, name, national_team_obj, club, dob):
        super().__init__(name, national_team_obj, club, dob, self.position)


if __name__ == '__main__':
    d = CentralAttackingMidfielder(
        name="Modric",
        national_team_obj="Croatia",
        club="Real Madrid",
        dob=""
    )
    print(d)
