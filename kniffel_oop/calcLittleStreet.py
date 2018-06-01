from scoreEntry import ScoreEntry
from collections import Counter

class CalcLittelStreet(ScoreEntry):

    def calculateKat(self, newDice):
        if self.isAllowed(newDice):
            self.points = 30

    def isAllowed(self, newDice):
        l = []
        
        for x in newDice:
            l.append(str(x.value))
        
        l = list(set(l))
        l.sort()
        s="".join(l)


        if ("3456" in s
        or "1234" in s
        or "2345" in s):
            return True
        return False