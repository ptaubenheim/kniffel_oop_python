
class FailureHandling:

    def inputFailure():
        while True:       
            try:
                chosenDice = [int(x)-1 for x in input().split()]
                break
            except ValueError:
                print("Bitte gebe deine Würfel erneut ein z.B. 1 2 3 4 5")
        return chosenDice