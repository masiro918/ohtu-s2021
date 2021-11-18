class Player:

    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.goals + self.assists

    def __str__(self):
        return_str = f"{self.name:30}" + self.team + f" {self.goals:2}" + ' + ' + f"{self.assists:2}" + ' = ' + f"{str(self.points):4}"
        return return_str
