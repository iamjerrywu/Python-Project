"""
File: bouncing_ball.py
Name: sheng-hao.wu
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

#objects as Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x = START_X, y = START_Y)
ball.filled = True
ball.filled_color = "black"

#Global constant helper
BALL_DROP_TIMES = 3
lock = False
ball_drop_count = 0

def ball_drop(mouse):
    global lock, ball_drop_count
    vy = 0
    mov_down = True

    #if not screen-click lock (before ball drop) and drop times less than three, go ball dropping
    if not lock and ball_drop_count < BALL_DROP_TIMES:
        lock = True
        ball_drop_count+=1
        # if ball is not out of x bound, keep looping simulating ball's movement
        while ball.x < window.width:
            # ball would only move down if y-axis velocity > 0
            if vy > 0:
                mov_down = True
            # when ball hits ground, velocity should change sign only once! use mov_down boolean to guarantee
            if (ball.y + SIZE) > window.height and mov_down:
                vy*=-REDUCE
                mov_down = False
            # no matter how ball moves upward or downward, gravity always impact positively, which is downward
            vy+=GRAVITY
            # move ball
            ball.move(VX, vy)
            # delay 10ms to simulate 1s in real world
            pause(DELAY)

        # once out of while loop (ball is out of range, reset back to original location
        ball.x = START_X
        ball.y = START_Y
        # unlock screen-click
        lock = False

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    onmouseclicked(ball_drop)

if __name__ == "__main__":
    main()
