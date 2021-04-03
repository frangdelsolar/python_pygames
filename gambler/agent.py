import random 
from slot import Slot

class Agent():
    def __init__(self):
        self.days = 0
        self.max_age = 79
        self.live = True
        self.risk = 35
        self.gamble_days = 0
        self.work_days = 0
        self.income = 0

    def update(self):
        self.decide()
        self.days += 1
        if self.days == self.max_age*365:
            self.die()

    def decide(self):
        r = random.randint(1, 100)
        if self.risk < r:
            self.go_work()
        else:
            self.go_gambling()
    
    def go_gambling(self):
        self.gamble_days += 1

        budget = 150
        self.income -= budget

        slot = Slot()
        coin_price = 5 
        rounds = budget/coin_price
        for i in range(int(rounds)):
            self.income += slot.play()


    def go_work(self):
        self.work_days += 1
        work_hours = 8
        wage = 30
        self.income += work_hours * wage

    def die(self):
        self.live = False
        print('You just die')

    def show(self):
        print('////////////////////////')
        print(self.days//360, 'años')
        print('Gamble days', self.gamble_days//81)
        print('Work days', self.work_days//81)
        print('Dinero disponible', self.income)
        print('////////////////////////')
