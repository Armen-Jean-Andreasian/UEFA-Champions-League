from __future__ import annotations
from players.player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from teams.nationals.team import NationalTeam
    from teams import NationalTeam, FootballClub


class Defender(Player):
    def __init__(self, name: str, nationality: NationalTeam, club: FootballClub, dob: str, position: str):
        super().__init__(name=name, national_team_obj=nationality, position=position, club_obj=club, date_of_birth=dob)

    def __str__(self):
        return super().__str__()


class CenterBack(Defender):
    position = "CB"

    def __init__(self, name: str, nationality: NationalTeam, club: FootballClub, dob: str):
        super().__init__(name=name, nationality=nationality, club=club, dob=dob, position=CenterBack.position)


class LeftBack(Defender):
    position = "LB"

    def __init__(self, name: str, nationality: NationalTeam, club: FootballClub, dob: str):
        super().__init__(name=name, nationality=nationality, club=club, dob=dob, position=LeftBack.position)


class RightBack(Defender):
    position = "RB"

    def __init__(self, name: str, nationality: NationalTeam, club: FootballClub, dob: str):
        super().__init__(name=name, nationality=nationality, club=club, dob=dob, position=RightBack.position)


if __name__ == '__main__':
    d = LeftBack(
        name="R. Carlos",
        nationality="Brazil",
        club="Real Madrid",
        dob=""
    )
    print(d)
