from players.player import Player


class Forward(Player):
    def __str__(self):
        return Player.__str__(self)


class CenterForward(Forward):
    def __init__(self, name, nationality, club, dob):
        super().__init__(name=name, nationality=nationality, position=CenterForward, club=club, date_of_birth=dob)


class LeftWinger(Forward):
    def __init__(self, name, nationality, club, dob):
        super().__init__(name=name, nationality=nationality, position=LeftWinger, club=club, date_of_birth=dob)


class RightWinger(Forward):
    def __init__(self, name, nationality, club, dob):
        super().__init__(name=name, nationality=nationality, position=RightWinger, club=club, date_of_birth=dob)


class Striker(Forward):
    def __init__(self, name, nationality, club, dob):
        super().__init__(name=name, nationality=nationality, position=Striker, club=club, date_of_birth=dob)


if __name__ == '__main__':
    d = Striker(
        name="Adriano",
        nationality="Brazil",
        club="Inter Milan",
        dob=""
    )
    print(d)
