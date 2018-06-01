from scoreEntry import ScoreEntry
from collections import Counter

class CalcFullHouse(ScoreEntry):

    def calculateKat(self, newDice):
        if self.isAllowed(newDice):
            self.points = 25

    def isAllowed(self, newDice):
        l = [x.value for x in newDice]
        cnt = Counter(l)
        print(cnt)
        for k, v in cnt.items():
            if v == 3:
                for k, v in cnt.items():
                    if v == 2:
                        return True
        return False
