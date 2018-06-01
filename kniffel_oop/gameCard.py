import game, die, player, sys
from scoreEntry import ScoreEntry
from calcPointsByDieValue import CalcDieValues
from calcThreePash import CalcThreePash
from calcFourPash import CalcFourPash
from calcKniffel import CalcKniffel
from calcLittleStreet import CalcLittelStreet
from calcGrandStreet import CalcGrandStreet
from calcFullHouse import CalcFullHouse

class GameCard():
    def __init__(self):        
        #self.__gameCard = {'1er': 0, '2er': 0, '3er': 0, '4er': 0, '5er': 0, '6er': 0, '3er-Pash': 0, '4er-Pash': 0, 'FullHouse': 0, 'kleineStraße': 0, 'großeStraße': 0, 'Kniffel': 0, 'Chance': 0, 'xtraKniffel': 0}
        self.__gameCard = {
            1: CalcDieValues("1er", 1),
            2: CalcDieValues("2er", 2),
            3: CalcDieValues("3er", 3),
            4: CalcDieValues("4er", 4),
            5: CalcDieValues("5er", 5),
            6: CalcDieValues("6er", 6),
            7: CalcThreePash("3er-Pash"),
            8: CalcFourPash("4er-Pash"),
            9: CalcFullHouse("FullHouse"),
            10: CalcLittelStreet("kleineStraße"),
            11: CalcGrandStreet("großeStraße"),
            12: CalcKniffel("Kniffel"),
            13: ScoreEntry("Chance"),
            14: CalcKniffel("xtraKniffel")
        }

    def resetGameCard(self):
        #    self.__gameCard = {'1er': 0, '2er': 0, '3er': 0, '4er': 0, '5er': 0, '6er': 0, '3er-Pash': 0, '4er-Pash': 0, 'FullHouse': 0, 'kleineStraße': 0, 'großeStraße': 0, 'Kniffel': 0, 'Chance': 0, 'xtraKniffel': 0}
        pass

    def isSomethingAvailable(self):
        print("in function isSomwhatFree")
        for k, v in self.__gameCard.items():
            if v.points == 0:
                return True
        return False 

    def writeScore(self, newDice):
        print("Wo sollen die Punkte hin?\n")
        
        print("Bitte gebe eine Kategorie ein")
        while True:
            try:
                katNum = int(input())
                break
            except (ValueError):
                print("Bitte gebe eine Zahl ein. Versuche es noch einmal ...")

        if (katNum in self.__gameCard):          

            if self.__gameCard[katNum].points != 0:
                print("FEHLER: ", katNum, "ist schon ausgespielt.\n\nBitte wähle eine andere Kategorie")
                self.writeScore(newDice)
            else:
                self.__gameCard[katNum].calculateKat(newDice)                
                print("Deine Punkte:", self.__gameCard[katNum].points)
                print("Punkte in GameCard", self.__gameCard[katNum])
                print(self.__gameCard)

    def calculatePoints(self):
        points = 0
        for k, v in self.__gameCard.items():
            points+=v.points
        return points
