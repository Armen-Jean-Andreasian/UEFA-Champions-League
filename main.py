from players import LeftBack
from teams import NationalTeam

if __name__ == '__main__':
    national_team = NationalTeam(country_name="Brazil")
    d = LeftBack(
        name="R. Carlos",
        nationality=national_team,
        club="Real Madrid",
        dob=""
    )
    print(d)
    print(national_team.get_list())