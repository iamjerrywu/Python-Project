"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Bricks Breakout Game!
Three lives and let's see how good you are!

author: sheng-hao wu
description: class/object/method defined file
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
MIN_X_SPEED = 1        # Minimum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) + brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) + brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width)/2, y=window_height - paddle_height - paddle_offset)
        self.obj_fill_color_add(self.paddle, "black")

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius, ball_radius, x=(window_width - ball_radius) / 2, y=(window_height - ball_radius)/2)
        self.obj_fill_color_add(self.ball, "black")

        # Default initial velocity and direction control for the ball.
        self.__dx = random.randint(MIN_X_SPEED, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        if self.__dx > 0:
            self.__dx_right = True
        else:
            self.__dx_right = False

        self.__dy = INITIAL_Y_SPEED
        self.__dy_down = True

        # Game flow control related
        self.ball_active = False
        self.remained_life = 0
        self.remained_bricks = brick_cols * brick_rows

        # Initialize our mouse listeners.
        #only when mouse clicked would active the game
        onmouseclicked(self.game_active)
        onmousemoved(self.move_paddle)

        # Draw bricks.
        # brick colors selections
        bricks_colors = ["red", "orange", "yellow", "green", "blue"]
        # init bricks[1] ~ bricks[101], bricks[0] no use leave it as "None"
        self.bricks = [None] * 101
        for col in range(1, brick_cols + 1):
            for row in range(1, brick_rows + 1):
                self.bricks[col * row] = GRect(brick_width, brick_height, x=col * (brick_spacing + brick_width) - brick_width, y=row * (brick_spacing + brick_height) - brick_height)
                self.obj_fill_color_add(self.bricks[col * row], bricks_colors[(row - 1)//2])

    # getter for ball dx
    def get_ball_dx(self):
        return self.__dx

    # setter for ball dx
    def set_ball_dx(self, val):
        self.__dx = val
        return self.__dx

    # getter for ball dx_right
    def get_ball_dx_right(self):
        return self.__dx_right

    # setter for ball dx_right
    def set_ball_dx_right(self, val):
        self.__dx_right = val
        return self.__dx_right

    # getter for ball dy
    def get_ball_dy(self):
        return self.__dy

    # setter for ball dy
    def set_ball_dy(self, val):
        self.__dy = val
        return self.__dy

    # getter for ball dy_down
    def get_ball_dy_down(self):
        return self.__dy_down

    # setter for ball dy_down
    def set_ball_dy_down(self, val):
        self.__dy_down = val
        return self.__dy_down

    # func for paddle track mouse.x position
    def move_paddle(self, mouse):
        if 0 + self.paddle.width/2 <= mouse.x <= self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width/2

    # func to active game
    def game_active(self, mouse):
        self.ball_active = True

    # reset ball's position
    def reset_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    # func helps fill and add object
    def obj_fill_color_add(self, obj, color):
        obj.color = color
        obj.filled = True
        obj.fill_color = color
        self.window.add(obj)
