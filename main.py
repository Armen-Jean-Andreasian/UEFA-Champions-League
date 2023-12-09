from players import *
from teams import NationalTeam, FootballClub

if __name__ == '__main__':
    # def welcome_choice():
    #     choice = input("Enter 1 to see the national team squad, \n"
    #                    "Enter 2 to see the club squad\n"
    #                    "Enter 3 to register a player")
    #     return choice
    #
    # def see_national_team(country_name):
    #     national_team_obj = NationalTeam(country_name=country_name)
    #     return national_team_obj.get_squad()
    #
    # def see_club(club_name):
    #     club_obj = FootballClub(club_name=club_name)
    #     return club_obj.get_squad()
    #
    # def create_player(position, name, nationality, club):
    #     national_team_obj = NationalTeam(country_name="Brazil")
    #     club_obj = FootballClub(club_name=club)
    #
    #     match position:
    #         case "LM":
    #             postion_obj = LeftMidfielder
    national_team_obj = NationalTeam(country_name="Brazil")
    d = LeftBack(
        name="R. Carlos",
        nationality=national_team_obj,
        club="Real Madrid",
        dob=""
    )
    national_team_obj.get_squad()
    # print(d)
    # print(national_team.get_squad())
