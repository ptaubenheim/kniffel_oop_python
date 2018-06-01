import die, gameCard
import FailureHandling

class Player():

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.newDice = []
        self.throws = 3
        self.scoreCard = gameCard.GameCard()

    def roll(self, dice):
        for x in dice:
            x.roll()
        self.throws -= 1
        print("ROLL-METHODE")


    def selectDie(self, dice):
       
        # Print new Dice
        print("\n")
        for x in self.newDice:
            print("Bereits ausgewählte Würfel:", x.value)


        print("Welche Würfel möchtest Du wählen?")

        
        chosenDice = FailureHandling.FailureHandling.inputFailure()
               
        # print("Du hast folgende Würfel gewählt", chosenDice) ##### __repr__ einfügen
        # print("Folgende Würfel wurden geworfen", dice)

        for die in chosenDice:
            self.newDice.append(dice[die])

        for die in self.newDice:
            if die.free:
                dice.remove(die)
                die.select()
            
        
        print("Du hast noch", len(dice), "Würfel\n")
        print("Du hast noch", self.throws, "Versuche")


    def writeScoreToGameCard(self):
        self.scoreCard.writeScore(self.newDice)
