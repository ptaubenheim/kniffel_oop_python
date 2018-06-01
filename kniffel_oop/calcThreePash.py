from scoreEntry import ScoreEntry
from collections import Counter

class CalcThreePash(ScoreEntry):

    def isAllowed(self, newDice):
        l = [x.value for x in newDice]
        cnt = Counter(l)
        print(cnt)
        for k, v in cnt.items():
            if v == 3:
                return True
        return False
