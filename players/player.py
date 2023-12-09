from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from teams.nationals.team import NationalTeam
    from teams import NationalTeam, FootballClub


class Player(ABC):
    player_instances = []

    def __init__(self, name: str, national_team_obj: NationalTeam, club_obj: FootballClub,
                 position=None, date_of_birth=None):
        # given
        self.name = name
        self.national_team_obj = national_team_obj
        self.club_obj = club_obj
        if date_of_birth: self.date_of_birth = date_of_birth

        # lifted
        self.position = position

        # attributes

        self.country_name = national_team_obj.country_name
        self.club_name = club_obj.club_name

        Player.player_instances.append(self)

    def __str__(self):
        return f"{self.name}, {self.national_team_obj.country_name}/{self.club_obj.club_name}, {self.position}"
