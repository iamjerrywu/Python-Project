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

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.dx*= -1
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.dy*=-1

        maybe_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        if maybe_obj:
            if maybe_obj.x + maybe_obj.width > graphics.ball.x:
                graphics.dy*=-1
            elif maybe_obj.x + maybe_obj.width == graphics.ball.x and maybe_obj.y + maybe_obj.height == graphics.ball.y:
                graphics.dx *= -1
                graphics.dy *= -1
            elif maybe_obj.y + maybe_obj.height >  graphics.ball.y:
                graphics.dx *= -1

        maybe_obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        if maybe_obj.x + maybe_obj.width > graphics.ball.x:
            graphics.dy *= -1
        elif maybe_obj.x + maybe_obj.width == graphics.ball.x and maybe_obj.y + maybe_obj.height == graphics.ball.y:
            graphics.dx *= -1
            graphics.dy *= -1
        elif maybe_obj.y + maybe_obj.height > graphics.ball.y:
            graphics.dx *= -1



        print("vx = ", graphics.dx, "vy = ", graphics.dy, "ball_x = ", graphics.ball.x, "ball_y = ", graphics.ball.y)

        #pause
        pause(FRAME_RATE)



if __name__ == '__main__':
    main()
