from teams.get_squad import PlayerManager


class FootballClub:
    def __init__(self, club_name, club_country=None):
        self.club_name = club_name
        self.club_country = club_country

    def __str__(self):
        return self.club_name

    def get_squad(self):
        return PlayerManager.sort_players_by_club(club_name=self.club_name)
