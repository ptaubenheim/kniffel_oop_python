from scoreEntry import ScoreEntry

class CalcDieValues(ScoreEntry):
    def __init__(self, name, allowedNumber):    
        super().__init__(name)
        self.allowedNumber = allowedNumber

    def calculateKat(self, newDice):
        if self.isAllowed(newDice):
            for x in newDice:
                if x.value == self.allowedNumber:
                    self.points+=x.value
            print("Punkte", self.points)

    def isAllowed(self, newDice):
        for x in newDice:
            if x.value == self.allowedNumber:
                return True
        return False
