# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
# [GCC 9.3.0]
# Embedded file name: /home/user/ohtu/tehtavat/ohtu-s2021/vk3/syksy2021-python-master/koodi/viikko3/nhl-reader/src/player.py
# Compiled at: 2021-11-16 19:22:12
# Size of source mod 2**32: 547 bytes


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