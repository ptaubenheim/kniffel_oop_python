#! /usr/bin/env python3
import die

class ScoreEntry:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.name + " " + str(self.points)

    def calculateKat(self, newDice):
        if self.isAllowed(newDice):
            for x in newDice:
                self.points+=x.value

    def isAllowed(self, newDice):
        return True
    