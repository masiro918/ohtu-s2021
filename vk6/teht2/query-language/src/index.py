from statistics import Statistics
from player_reader import PlayerReader
from matchers import Not, HasFewerThan, And, HasAtLeast, PlaysIn

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    '''
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )
    '''
    matcher = And(
        #HasAtLeast(1, "goals"),
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )


    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()