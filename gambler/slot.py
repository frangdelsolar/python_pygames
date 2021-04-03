import random

class Slot:
    def __init__(self):
        self.reel1 = ['banana', 'lemon', 'orange', 'apple', 'melon', 'jocker']
        self.reel2 = ['banana', 'lemon', 'orange', 'apple', 'melon', 'jocker']
        self.reel3 = ['banana', 'lemon', 'orange', 'apple', 'melon', 'jocker']

    def randomize(self):
        c1 = random.choice(self.reel1)
        c2 = random.choice(self.reel2)
        c3 = random.choice(self.reel3)
        return [c1, c2, c3]

    def play(self):
        pay = 0

        c1, c2, c3 = self.randomize()

        if c1 == c2 == c3 == 'jocker':
            pay = 30

        elif ((c1 == c2 != c3 and c1 != 'jocker') or
            (c1 == c3 != c2 and c1 != 'jocker') or
            (c2 == c3 != c1 and c2 != 'jocker') ):
            pay = 10

        elif ((c1 == c2 == 'jocker' != c3) or
            (c2 == c3 == 'jocker' != c1) or
            (c1 == c3 == 'jocker' != c2)):
            pay = 4

        elif ((c1 == 'jocker' != c2 != c3) or
            (c2 == 'jocker' != c1 != c3) or
            (c3 == 'jocker' != c1 != c2)):
            pay = 1

        return pay
