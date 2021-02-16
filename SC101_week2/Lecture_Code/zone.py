from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 1000 / 240 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone'
    A ball will be bouncing around the GWindow
    Players must defend the zone indicated by black
    line at the middle of the GWindow by clicking on
    the bouncing ball
    """
    graphics = ZoneGraphics()
    print("y_1st=",0, "y_2nd=", graphics.zone.y, "y_3rd=", graphics.zone.y + graphics.zone.height, "y_4th=", graphics.window.height)
    graphics.set_ball_position()
    graphics.set_ball_velocity()
    while True:
        graphics.ball.move(graphics.dx, graphics.dy)

        # check
        if graphics.dx > 0:
            graphics.dx_right = True
        else:
            graphics.dx_right = False
        if graphics.dy > 0:
            graphics.dy_down = True
        else:
            graphics.dy_down = False

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.dx*= -1
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.dy*=-1

        if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) and graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height) and graphics.dx_right is False:
            graphics.dx*=-1
            graphics.dx_right = True
        if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y) and graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height) and graphics.dx_right is True:
            graphics.dx *= -1
            graphics.dx_right = False
        if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) and graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y) and graphics.dy_down is False:
            graphics.dy*=-1
            graphics.dy_down = True
        if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height) and graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height) and graphics.dy_down is True:
            graphics.dy *= -1
            graphics.dy_down = False

        print("vx = ", graphics.dx, "vy = ", graphics.dy, "ball_x = ", graphics.ball.x, "ball_y = ", graphics.ball.y)

        #pause
        pause(FRAME_RATE)



if __name__ == '__main__':
    main()
