import random
import random
import time

ANIMATION_CHARS = "/|-\\"

def animatedDice():
    idx = 0
    while idx < 10:
        print(ANIMATION_CHARS[idx % len(ANIMATION_CHARS)], end = '\r')
        idx += 1
        time.sleep(0.05)

class Die():
    def __init__(self, value=0):
        self.value = value
        self.free = True

    def roll(self):
        animatedDice()
        self.value = random.randint(1,6)

    def select(self):
        self.free = False