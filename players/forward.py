from __future__ import annotations
from players.player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from teams.nationals.team import NationalTeam
    from teams import NationalTeam, FootballClub


class Forward(Player):
    def __str__(self):
        return super().__str__()


class CenterForward(Forward):
    position = "CF"

    def __init__(self, name, national_team_obj: NationalTeam, club: FootballClub, dob):
        super().__init__(name, national_team_obj, club, dob, CenterForward.position)


class LeftWinger(Forward):
    position = "LW"

    def __init__(self, name, national_team_obj: NationalTeam, club: FootballClub, dob):
        super().__init__(name, national_team_obj, club, dob, LeftWinger.position)


class RightWinger(Forward):
    position = "RW"

    def __init__(self, name, national_team_obj: NationalTeam, club: FootballClub, dob):
        super().__init__(name, national_team_obj, club, dob, RightWinger.position)


class Striker(Forward):
    position = "ST"

    def __init__(self, name, national_team_obj: NationalTeam, club: FootballClub, dob):
        super().__init__(name, national_team_obj, club, dob, Striker.position)


if __name__ == '__main__':
    from teams import *
    country = "Brazil"
    fc = "Inter"

    national_team_obj_ = NationalTeam(country)
    club_obj_ = FootballClub(club_name=fc)
    d = Striker(
        name="Adriano",
        national_team_obj=national_team_obj_,
        club=club_obj_,
        dob=""
    )

    one = PlayerManager.sort_players_by_nationality(country)
    print(one)
    two = PlayerManager.sort_players_by_club(fc)
    print(two)
    print(d)
