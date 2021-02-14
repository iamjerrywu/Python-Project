from campy.graphics.gobjects import GOval, GRect

class Robot:
    # Constructor
    def __init__(self, height, weight, color = "green"):
        print(__name__)
        self.h = height
        self.w = weight
        self.c = color
        self.ball = None


    #method
    def give_me_a_ball(self, size):
        self.ball = GOval(size, size)
        self.ball.filled = True
        self.ball.fill_color = self.c
        print("I have a ball, size: ", self.ball.width)

    def speak(self):
        print("my height = ", self.h, "my weight = ", self.w)

    def self_intro(self):
        print(f'h = {self.h}/w={self.w}')

    def bmi(self):
        return self.w/self.h**2

    def say_hi1(self):
        print("hi")
    @staticmethod
    def say_hi2():
        print("hihi")

    class RobotArm:
        def __init__(self, property, length):
            self.property = property
            self.length = length

class Robot2(Robot):
    def __init__(self, height2, weight2, color2 = "red", count2 = 3):
        super().__init__(height2, weight2, color = color2)
        self.count2 = count2

    def start_count(self):
        for i in range(self.count2):
             print(i)

class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color3, color3 = "green", count3 = 3):
        super().__init__(height3, weight3, color2 = color3, count2 = count3)
        self.r_c = rect_color3

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect

