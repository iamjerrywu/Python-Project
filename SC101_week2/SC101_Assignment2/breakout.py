"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3

# func for setting up ball's right direction parameters
def direction_check(obj):
    if obj.get_ball_dx() > 0:
        obj.set_ball_dx_right(True)
    else:
        obj.set_ball_dx_right(False)
    if obj.get_ball_dy() > 0:
        obj.set_ball_dy_down(True)
    else:
        obj.set_ball_dy_down(False)

# func for ensuring ball's within window
def boundary_check(obj):
    if obj.ball.x <= 0 or obj.ball.x + obj.ball.width >= obj.window.width:
        obj.set_ball_dx(-obj.get_ball_dx())
    if obj.ball.y <= 0:
        obj.set_ball_dy(-obj.get_ball_dy())
    elif obj.ball.y >= obj.window.height:
        obj.ball_active = False
        obj.remained_life-=1


def collisions_handler(obj):
    # check for ball's left side
    rm_obj = obj.window.get_object_at(obj.ball.x, obj.ball.y) and obj.window.get_object_at(obj.ball.x, obj.ball.y + obj.ball.height)
    if rm_obj and obj.get_ball_dx_right() is False:
        rm_obj_and_change_ball_dir(rm_obj, obj, -obj.get_ball_dx(), True, obj.get_ball_dy(), obj.get_ball_dy_down())

    # check for ball's right side
    rm_obj = obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y) and obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y + obj.ball.height)
    if rm_obj and obj.get_ball_dx_right() is True:
        rm_obj_and_change_ball_dir(rm_obj, obj, -obj.get_ball_dx(), False, obj.get_ball_dy(), obj.get_ball_dy_down())

    # check for ball's up side
    rm_obj = obj.window.get_object_at(obj.ball.x, obj.ball.y) and obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y)
    if rm_obj and obj.get_ball_dy_down() is False:
        rm_obj_and_change_ball_dir(rm_obj, obj, obj.get_ball_dx(), obj.get_ball_dx_right(), -obj.get_ball_dy(), True)

    # check for ball's down side
    rm_obj = obj.window.get_object_at(obj.ball.x, obj.ball.y + obj.ball.height) and obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y + obj.ball.height)
    if rm_obj and obj.get_ball_dy_down() is True:
        rm_obj_and_change_ball_dir(rm_obj, obj, obj.get_ball_dx(), obj.get_ball_dx_right(), -obj.get_ball_dy(), False)


def rm_obj_and_change_ball_dir(rm_obj, obj, dx, dx_right, dy, dy_down):
    if rm_obj is not obj.paddle:
        obj.window.remove(rm_obj)
        obj.remained_bricks-=1
    obj.set_ball_dx(dx)
    obj.set_ball_dx_right(dx_right)
    obj.set_ball_dy(dy)
    obj.set_ball_dy_down(dy_down)

def main():
    graphics = BreakoutGraphics()
    graphics.remained_life = NUM_LIVES
    print()
    while True:
        if graphics.ball_active:
            # check and setup balls into right direction
            direction_check(graphics)

            # move ball
            graphics.ball.move(graphics.get_ball_dx(), graphics.get_ball_dy())

            # check for collision and handler ball's direction
            collisions_handler(graphics)

            # ball should withinR window boundary, and would end game if out of window's low bound
            boundary_check(graphics)
            if not graphics.ball_active:
                if graphics.remained_life == 0:
                    break
                else:
                    graphics.reset_ball_position()

            if graphics.remained_bricks == 0:
                break

        pause(FRAME_RATE)

if __name__ == '__main__':
    main()
