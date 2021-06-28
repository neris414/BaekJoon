#타임아웃 발생..

import sys

class portfolio:
    def __init__(self, predict):
        self.predict = [int(i) for i in predict.split()]
        self.history = []
        self.money = 0
    
    def buy(self):
        self.history.append(self.predict[0])
        self.money -= self.predict[0]
        del self.predict[0]

    def nothing(self):
        del self.predict[0]

    def sell(self):
        self.money += (self.predict[0]*len(self.history))
        self.history = []
        del self.predict[0]

    
    def optimal(self):
        for i in range(len(self.predict)):
            if (self.predict[0] < max(self.predict)):
                self.buy()
            elif (self.predict[0] == max(self.predict)):
                self.sell()
            else:
                self.nothing()
        return self.money

if __name__ == "__main__":
    testcase = int(input())
    result = []
    for i in range(testcase):
        predict_day = int(input())
        predict = input()
        result.append(portfolio(predict).optimal())
    for i in result:
        print(i)
