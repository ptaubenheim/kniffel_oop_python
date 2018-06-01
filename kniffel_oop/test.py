#! /usr/bin/env python3
import die, game


class Test:
    def __init__(self):
        self.kat = 3
        self.points = 0
        self.newDice = {"eins" : 1, "zwei" : 2, "drei": 1, "vier": 3, "funf": 5, "sechs": 3}

    def calculateKat(self):
        print("in calc kat")
        if self.isAllowed():
            for x in self.newDice:
                if self.newDice[x] == self.kat:
                    print("ich berechne")
                    self.points+=self.newDice[x]
            print(self.points)

    def isAllowed(self):
        if self.kat in range(1,6):
            for x in self.newDice:
                if self.newDice[x] == self.kat:
                    print("True")
                    return True
        else:
            print("False")
            return False

    def play(self):
        self.calculateKat()



    #################
def main():
    test = Test()
    test.play()

if __name__=="__main__":
    main()