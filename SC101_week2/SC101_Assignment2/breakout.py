"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Bricks Breakout Game!
Three lives and let's see how good you are!

author: sheng-hao wu
description: animations-related file
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3

# func for checking boundary
def boundary_check(obj):
    # ensure ball's is within window and handles it's direction
    if obj.ball.x <= 0 and obj.get_ball_dx_right() is False or obj.ball.x + obj.ball.width >= obj.window.width and obj.get_ball_dx_right() is True:
        obj.set_ball_dx(-obj.get_ball_dx())
        obj.set_ball_dx_right(not obj.get_ball_dx_right())
    if obj.ball.y <= 0 and obj.get_ball_dy_down() is False:
        obj.set_ball_dy(-obj.get_ball_dy())
        obj.set_ball_dy_down(True)
    # if ball's out of window's low bound, life count - 1 and pause the game
    elif obj.ball.y >= obj.window.height:
        obj.ball_active = False
        obj.remained_life-=1

def collisions_handler(obj):
    change_dx = False
    change_dy = False

    """
    algorithm for handling collision:
        1. identify whether hit object in ball's four vertices respectively
            a. if yes, then identify the ball's relevant position to the object that it collides
                i. calculate the ball's previous position before collide, prev_pos(x,y) = cur_pos(x +/- abs(dx), y+/- abs(dy))
            b. based on the relationship between ball's previous position and the collide object, then change ball's direction
    """
    #upper-left point:
    rm_obj = obj.window.get_object_at(obj.ball.x, obj.ball.y)
    if rm_obj and rm_obj is not obj.ball:
        if obj.ball.x + abs(obj.get_ball_dx()) > rm_obj.x + rm_obj.width and obj.get_ball_dx_right() is False:
            change_dx = True
        if obj.ball.y + abs(obj.get_ball_dy()) >= rm_obj.y + rm_obj.height and obj.get_ball_dy_down() is False:
            change_dy = True
        # remove object
        rm_obj_handler(rm_obj, obj)

    # down-left point:
    rm_obj = obj.window.get_object_at(obj.ball.x, obj.ball.y + obj.ball.height)
    if rm_obj and rm_obj is not obj.ball:
        if obj.ball.x + abs(obj.get_ball_dx()) > rm_obj.x + rm_obj.width and obj.get_ball_dx_right() is False:
            change_dx = True
        if obj.ball.y + obj.ball.height - abs(obj.get_ball_dy()) < rm_obj.y and obj.get_ball_dy_down() is True:
            change_dy = True
        # remove object
        rm_obj_handler(rm_obj, obj)

    # down-right point:
    rm_obj = obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y + obj.ball.height)
    if rm_obj and rm_obj is not obj.ball:
        if obj.ball.x + obj.ball.width - abs(obj.get_ball_dx()) < rm_obj.x and obj.get_ball_dx_right() is True:
            change_dx = True
        if obj.ball.y + obj.ball.height - abs(obj.get_ball_dy()) < rm_obj.y and obj.get_ball_dy_down() is True:
            change_dy = True
        # remove object
        rm_obj_handler(rm_obj, obj)

    # up-right point:
    rm_obj = obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y)
    if rm_obj and rm_obj is not obj.ball:
        if obj.ball.x + obj.ball.width - abs(obj.get_ball_dx()) < rm_obj.x and obj.get_ball_dx_right() is True:
            change_dx = True
        if obj.ball.y + abs(obj.get_ball_dy()) >= rm_obj.y + rm_obj.height and obj.get_ball_dy_down() is False:
            change_dy = True
        # remove object
        rm_obj_handler(rm_obj, obj)

    # change ball's direction
    dx = -obj.get_ball_dx() if change_dx is True else obj.get_ball_dx()
    dy = -obj.get_ball_dy() if change_dy is True else obj.get_ball_dy()
    if change_dx or change_dy:
        change_dir_handler(obj, dx, dy)

# remove object
def rm_obj_handler(rm_obj, obj):
    if rm_obj is not obj.paddle:
        obj.window.remove(rm_obj)
        obj.remained_bricks-=1

# change ball's direction
def change_dir_handler(obj, dx, dy):
    obj.set_ball_dx(dx)
    obj.set_ball_dy(dy)
    if obj.get_ball_dx() > 0:
        obj.set_ball_dx_right(True)
    else:
        obj.set_ball_dx_right(False)
    if obj.get_ball_dy() > 0:
        obj.set_ball_dy_down(True)
    else:
        obj.set_ball_dy_down(False)

def main():
    graphics = BreakoutGraphics()
    # init remained life
    graphics.remained_life = NUM_LIVES
    while True:
        if graphics.ball_active:

            # move ball
            graphics.ball.move(graphics.get_ball_dx(), graphics.get_ball_dy())

            # check for collision and handler ball's direction
            collisions_handler(graphics)

            # ball should withinR window boundary, and would end game if it's out of window's low bound
            boundary_check(graphics)
            if not graphics.ball_active:
                if graphics.remained_life == 0:
                    break
                else:
                    graphics.reset_ball_position()
            # if no bricks remaining, gave over
            if graphics.remained_bricks == 0:
                break

        pause(FRAME_RATE)

if __name__ == '__main__':
    main()
