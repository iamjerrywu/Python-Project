
WITHDRAW_LIMIT = 1000
INITIAL_MONEY = 0


class Pypal:
    def __init__(self, username, money = INITIAL_MONEY, withdraw_limit = WITHDRAW_LIMIT):
        self.__un = username
        self.__m = money
        self.__w_l = withdraw_limit

    # def withdraw(self, amount):
    #     if amount > self.w_l:
    #         print("exceed limit!")
    #     elif self.m - amount < 0:
    #         print("illegal!")
    #     else:
    #         self.m-=amount
    #         print(f'{self.un}:{self.m}')
    def getmoney(self):
        return self.__m
    def withdraw(self, amount):
        if amount > self.__w_l:
            print("exceed limit!")
        elif self.__m - amount < 0:
            print("illegal!")
        else:
            self.__m-=amount
            print(f'{self.__un}:{self.__m}')


    def change_name(self, name):
        self.__un = name
    def show_name(self):
        print(self.__un)


def bank():
    jerry_a = Pypal('shenghao', money = 1000, withdraw_limit = WITHDRAW_LIMIT)
    # jerry_a.withdraw(4000) #exceed limit
    # jerry_a.withdraw(500) # shenghao: 500
    # jerry_a.withdraw(600) # illegal

    print(jerry_a.getmoney())
    jerry_a.show_name()
    jerry_a.withdraw(300)
    jerry_a.change_name("Jerry Wu")
    jerry_a.show_name()
    jerry_a.withdraw(800)
    print(jerry_a._Pypal__m)




if __name__ == '__main__':
    bank()


