from players import LeftBack
from teams import NationalTeam

if __name__ == '__main__':
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
