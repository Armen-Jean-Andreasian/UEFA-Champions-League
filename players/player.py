from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from teams.nationals.team import NationalTeam


class Player(ABC):
    player_instances = []

    def __init__(self, name, national_team_obj: NationalTeam, position, club, date_of_birth):
        self.name = name
        self.country = national_team_obj.country_name
        self.position = position
        self.club = club
        self.date_of_birth = date_of_birth
        Player.player_instances.append(self)

    def __str__(self):
        return f"{self.name}, {self.country}, {self.position}"
