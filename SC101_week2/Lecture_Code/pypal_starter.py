from pypal import Pypal

def bank():
    jerry_a = Pypal('shenghao', money =1000, withdraw_limit=2000)
    jerry_a.withdraw(2000)

if __name__ == '__main__'