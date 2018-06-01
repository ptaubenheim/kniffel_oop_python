from scoreEntry import ScoreEntry
from collections import Counter

class CalcGrandStreet(ScoreEntry):

    def calculateKat(self, newDice):
        if self.isAllowed(newDice):
            self.points = 40

    def isAllowed(self, newDice):
        l = []
        for x in newDice:
            l.append(str(x.value))
            
        l.sort()

        s = "".join(l)

        if ("12345" in s
        or "23456"):
            return True
        return False    