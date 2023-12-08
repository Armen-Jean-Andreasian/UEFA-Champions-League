class StartingSquad:
    def __init__(self, players_list):
        pass


class FormationsCatalog:
    def __init__(self):
        self.available_formations = {
            '4-3-3': ("GK", "CB", "CB", "LB", "RB", "CM", "CM", "CM", "RW", "ST", "LW"),
            '4-2-3-1': (),
        }

    def generate_4_3_3(self):
        return self.available_formations['4-3-3']

    def __str__(self):
        formations_str = ', '.join(self.available_formations.keys())
        return f"Available formations: {formations_str}"


class LineUp:
    def __init__(self, team_list, desired_formation):
        self.team_list = team_list
        self.desired_formation = desired_formation
        self.line_up = None
        self.starting_eleven = None

    def get_formation(self):
        formations_catalog = FormationsCatalog()
        if self.desired_formation in formations_catalog.available_formations:
            self.line_up = formations_catalog.available_formations[self.desired_formation]
        else:
            raise ValueError(formations_catalog.__str__())


if __name__ == '__main__':
    team = ""
    d = '4-3-2'
    l = LineUp(team, d)
    l.get_formation()
