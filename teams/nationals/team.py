from players import Player


class Country:
    def __init__(self, country_name):
        self.country_name = country_name


class NationalTeam(Country):
    def __init__(self, country_name):
        super().__init__(country_name)
        self.squad: tuple[Player] = None
