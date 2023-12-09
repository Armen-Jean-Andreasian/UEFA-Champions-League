from players import PlayerManager


class Country(object):
    def __init__(self, country_name):
        self.country_name = country_name

    def __str__(self):
        return str(self.country_name)


class NationalTeam(Country):
    def __init__(self, country_name):
        super().__init__(country_name)

    def get_squad(self):
        return PlayerManager.sort_players_by_nationality(country_name=self.country_name)

