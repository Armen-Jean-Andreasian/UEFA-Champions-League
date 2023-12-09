from players.player import Player


class PlayerManager:
    @staticmethod
    def sort_players_by_nationality(country_name: str):
        squad = [player.name for player in Player.player_instances if player.national_team_obj.country_name == country_name]
        return squad

    @staticmethod
    def sort_players_by_club(club_name):
        squad = [player.name for player in Player.player_instances if player.club_obj.club_name == club_name]
        return squad
