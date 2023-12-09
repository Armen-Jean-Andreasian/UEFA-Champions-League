from players.player import Player


class PlayerManager:
    @staticmethod
    def sort_players_by_nationality(country_name: str):
        my_list = Player.player_instances
        print(my_list)
        countries = [player.country for player in my_list]
        print(countries)
        names = [player.name for player in Player.player_instances if player]
        print(names)

    @staticmethod
    def sort_players_by_club(club_name):
        squad = list(filter(lambda x: x.club == club_name, Player.player_instances))
        return squad
