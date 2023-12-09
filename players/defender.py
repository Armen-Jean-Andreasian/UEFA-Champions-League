from players.player import Player


class Defender(Player):
    def __init__(self, name: str, nationality: object, club, dob: str, position: str):
        super().__init__(name=name, national_team_obj=nationality, club=club, date_of_birth=dob, position=position)

    def __str__(self):
        return super().__str__()


class CenterBack(Defender):
    def __init__(self, name: str, nationality: object, club, dob: str):
        position = "CB"
        super().__init__(name=name, nationality=nationality, club=club, dob=dob, position=position)


class LeftBack(Defender):
    def __init__(self, name: str, nationality: object, club, dob: str):
        position = "LB"
        super().__init__(name=name, nationality=nationality, club=club, dob=dob, position=position)
        # super().__init__(name=name, nationality=nationality, club=club, dob=dob, position=position)


class RightBack(Defender):
    def __init__(self, name: str, nationality: object, club, dob: str):
        position = "RB"
        super().__init__(name=name, nationality=nationality, club=club, dob=dob, position=position)


if __name__ == '__main__':
    d = LeftBack(
        name="R. Carlos",
        nationality="Brazil",
        club="Real Madrid",
        dob=""
    )
    print(d)
