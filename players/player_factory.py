from players import *
from teams import NationalTeam, FootballClub


class PlayerCreator:
    list_of_positions = [
        CentralMidfielder, CentralAttackingMidfielder, LeftMidfielder, RightMidfielder, DefenciveMidfielder,
        CenterBack, RightBack, LeftBack,
        Striker, LeftWinger, RightWinger

    ]

    def create_player(self, name, position, nationality, club, dob=None):
        player_obj = object()
        for pos in self.list_of_positions:
            if position == pos.position:
                player_obj = pos.__class__

        player = player_obj(
            name=name,
            national_team_obj=NationalTeam(country_name=nationality),
            club=FootballClub(club_name=club),
            position=position,
            date_of_birth=dob
        )
        return player


if __name__ == '__main__':
    p = PlayerCreator()
    pp = p.create_player(
        name="Ronaldo",
        nationality="Brazil",
        club="Real Madrid",
        position="ST"
    )
    print(pp)
