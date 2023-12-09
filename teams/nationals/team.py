from players import Player


class Country:
    def __init__(self, country_name):
        self.country_name = country_name

    def __str__(self):
        return str(self.country_name)


class NationalTeam(Country):

    def __init__(self, country_name):
        super().__init__(country_name)
        self.squad: tuple[Player] = None

    def get_list(self):
        player_objs_of_one_nationality = list(filter(lambda x: x.nationality == self, Player.player_instances))
        player_names = [player.name for player in player_objs_of_one_nationality]
        return player_names
