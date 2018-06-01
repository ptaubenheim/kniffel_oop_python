#! /usr/bin/env python3
import die, player, gameCard

class Game:
    def __init__(self):
        self.dice = [die.Die() for x in range(5)]
        self.player1 = player.Player("Patrick")

    def printDice(self):
        i = 1
        print("Deine Würfel haben folgende Werte\n")
        for x in self.dice:
            print("Würfel", i, ": ", x.value)
            i+=1

    def printPlayer(self):
        print("Hallo", self.player1.name, "Du hast: ", self.player1.points, " Punkte")

    def begin(self):
        self.dice = [die.Die() for x in range(5)]
        self.player1.newDice = []
        self.player1.throws = 3
        self.run()

    def end(self, points):
        print("Du hast ", points, "Punkte erzielt.\nMöchtest Du noch einmal spielen")
        if input() == "j":
            self.start()
        else:
            print("In Hamburg sagt man Tschüß, dass heißt Auf Wiedersehen")
            exit()

    def run(self):

        while True:
            print("\nDrücke eine Taste zum würfeln")
            s = input()

            if (s == "s"):
                break
            
            self.player1.roll(self.dice)
            self.printDice()
            self.player1.selectDie(self.dice)

            print("Länge von Dice", len(self.dice))
            if len(self.dice) == 0 or self.player1.throws == 0:
                self.player1.writeScoreToGameCard()
            else:
                continue

            if self.player1.scoreCard.isSomethingAvailable():
                self.begin()
            else:
                points = self.player1.scoreCard.calculatePoints()
                self.end(points)

    def start(self):
        self.player1.scoreCard.resetGameCard()
        print("Herzlich Willkommen zu einer neuen Runde KNIFFEL!!! \n\n")
        self.printPlayer()
        self.printDice()

        self.begin()


def main():
    game = Game()
    game.start()
        

if __name__=="__main__":
    main()