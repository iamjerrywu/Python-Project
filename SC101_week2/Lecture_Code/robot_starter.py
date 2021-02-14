#since robot is in the same directory as robot_starter.py
from robot import Robot, Robot2, Robot3
from campy.graphics.gwindow import GWindow

SIZE = 50
WINDOW_SIZE = 500
def main():
    window = GWindow(500, 500)
    r1 = Robot(188, 80, color = 'black')
    r1.give_me_a_ball(SIZE)
    print(__name__)
    # r1.speak()
    # r1.self_intro()
    # print(r1.bmi())
    # window.add(r1.ball, window.width/2 - SIZE/2, window.height/2 - SIZE/2)
    # print(r1.ball.width)
    # r1.say_hi1()
    # Robot.say_hi2()
    #
    #
    # right_r1_arm = r1.RobotArm("right", 100)
    # print(right_r1_arm.property, "arm length = ", right_r1_arm.length)

    r2 = Robot2(200, 300, color2 = "brown", count2 = 5)
    r2.start_count()
    r2.say_hi1()
    r2.say_hi2()
    r2.self_intro()

    r3 = Robot3(300, 400, "pink", color3 = "black", count3 = 100)
    r3.bmi()
    rect = r3.give_me_a_rect(20)
    r3.give_me_a_ball(SIZE)
    window.add(r1.ball, window.width/2 - SIZE/2, window.height/2 - SIZE/2)
    window.add(rect, window.width/2 - SIZE/2, window.height/2 - SIZE/2)

if __name__ == '__main__':
    main()