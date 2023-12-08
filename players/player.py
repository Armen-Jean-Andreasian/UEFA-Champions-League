from abc import ABC


class Player(ABC):
    def __init__(self, name, nationality, position, club, date_of_birth):
        self.name = name
        self.nationality = nationality
        self.position = position
        self.club = club
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.name}, {self.nationality}, {self.position}"



