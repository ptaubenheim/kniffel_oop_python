from scoreEntry import ScoreEntry
from collections import Counter

class CalcKniffel(ScoreEntry):

    def calculateKat(self, newDice):
        if self.isAllowed(newDice):
            self.points = 50

    def isAllowed(self, newDice):
        l = [x.value for x in newDice]
        cnt = Counter(l)
        print(cnt)
        for k, v in cnt.items():
            if v == 5:
                return True
        return False