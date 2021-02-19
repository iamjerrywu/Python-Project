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
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 10      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 80        # Width of a brick (in pixels).
BRICK_HEIGHT = 30       # Height of a brick (in pixels).
BRICK_ROWS = 5          # Number of rows of bricks.
BRICK_COLS = 10         # Number of columns of bricks.
BRICK_OFFSET = 50       # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10        # Radius of the ball (in pixels).
PADDLE_WIDTH = 150      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15      # Height of the paddle (in pixels).
PADDLE_OFFSET = 50      # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 3.0   # Initial vertical speed for the ball.
MAX_X_SPEED = 0         # Maximum initial horizontal speed for the ball.
MIN_X_SPEED = 0         # Minimum initial horizontal speed for the ball.
NUM_LIVES   = 3         # Number of lives
CANNON_BASE_WIDTH = 30  # Width of cannon base
CANNON_BASE_HEIGHT = 8  # Height of cannon base
CANNON_TUBE_WIDTH = 10  # Width of cannon tube
CANNON_TUBE_HEIGHT = 20 # Height of cannon tube
OUTER_FLAME_WIDTH = 30   # Width of outer flame
INNER_FLAME1_WIDTH = 20  # Width of inner flame
INNER_FLAME2_WIDTH = 15  # Width of inner flame
CANNON_ICON_Y_SPEED = 2  # Cannon icon y speed
CANNON_ICON_X_SPEED = 0  # Cannon icon x speed



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
        # self.ball = GOval(ball_radius, ball_radius, x=(window_width - ball_radius) / 2, y=(window_height - ball_radius)/2)
        self.ball = GOval(ball_radius, ball_radius, x=(window_width - ball_radius),
                          y=(window_height - ball_radius) / 2)

        self.obj_fill_color_add(self.ball, "black")

        # Score label
        self.score = 0
        self.score_label = GLabel("Score: " + str(self.score), 100, 200)
        self.score_label.font = "monospace-30-bold"
        self.window.add(self.score_label, 10, self.window.height - 10)

        # life icon
        self.num_lives = NUM_LIVES
        self.life_icons = [None] * 3
        for i in range(self.num_lives):
            self.life_icons[i] = GImage("heart_icon.jpeg")
            self.window.add(self.life_icons[i], self.window.width - ( self.life_icons[i].width * (3 - i)), self.window.height - self.life_icons[i].height - 12)


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
        self.remained_life = self.num_lives
        self.remained_bricks = brick_cols * brick_rows

        # Initialize our mouse listeners.
        #only when mouse clicked would active the game
        onmouseclicked(self.game_active)
        onmousemoved(self.move_paddle)

        # Draw bricks.
        # brick colors-score dictionary
        bricks_colors = ["midnightblue", "mediumblue", "blue", "dodgerblue", "lightskyblue"]
        # init bricks[1] ~ bricks[101], bricks[0] no use leave it as "None"
        self.bricks = [None] * 101
        for col in range(1, brick_cols + 1):
            for row in range(1, brick_rows + 1):
                self.bricks[col * row] = GRect(brick_width, brick_height, x=col * (brick_spacing + brick_width) - brick_width, y=row * (brick_spacing + brick_height) - brick_height)
                self.obj_fill_color_add(self.bricks[col * row], bricks_colors[row - 1])
                self.bricks[col * row].color_str = bricks_colors[row - 1]

        # Gave over label
        self.over_label = GLabel("Game Over")
        self.over_label.color = "red"
        self.over_label.font = "italic-100-bold"

        # create paddle cannon.
        self.cannon_base = GRect(CANNON_BASE_WIDTH, CANNON_BASE_HEIGHT, x=(window_width - CANNON_BASE_WIDTH) / 2, y=window_height - paddle_height - paddle_offset - CANNON_BASE_HEIGHT)
        self.cannon_base.color = "black"
        self.cannon_base.filled = True
        self.cannon_base.fill_color = "black"

        self.cannon_tube = GRect(CANNON_TUBE_WIDTH, CANNON_TUBE_HEIGHT, x=(window_width - CANNON_TUBE_WIDTH) / 2, y=window_height - paddle_height - paddle_offset - CANNON_BASE_HEIGHT - CANNON_TUBE_HEIGHT)
        self.cannon_tube.color = "black"
        self.cannon_tube.filled = True
        self.cannon_tube.fill_color = "black"

        # create cannon flame
        self.outer_flame = GRect(OUTER_FLAME_WIDTH, self.cannon_tube.y, x=(window_width - OUTER_FLAME_WIDTH) / 2, y=0)
        self.outer_flame.color = "red"
        self.outer_flame.filled = True
        self.outer_flame.fill_color = "red"
        # self.obj_fill_color_add(self.outer_flame, "red")
        self.inner_flame_1 = GRect(INNER_FLAME1_WIDTH, self.cannon_tube.y, x=(window_width - INNER_FLAME1_WIDTH) / 2, y=0)
        self.inner_flame_1.color = "yellow"
        self.inner_flame_1.filled = True
        self.inner_flame_1.fill_color = "yellow"
        # self.obj_fill_color_add(self.inner_flame_1, "yellow")
        self.inner_flame_2 = GRect(INNER_FLAME2_WIDTH, self.cannon_tube.y, x=(window_width - INNER_FLAME2_WIDTH) / 2, y=0)
        self.inner_flame_2.color = "lightyellow"
        self.inner_flame_2.filled = True
        self.inner_flame_2.fill_color = "lightyellow"
        # self.obj_fill_color_add(self.inner_flame_2, "lightyellow")

        # self.cannon_brick_index = random.randint(41, 50)
        self.cannon_brick_index = 50

        self.cannon_appear = False
        self.cannon_icon = GImage("cannon_icon.jpeg")
        self.cannon_icon_background = GRect(self.cannon_icon.width, self.cannon_icon.height)
        self.cannon_icon_background.filled = True
        self.cannon_icon_background.fill_color = "black"

        self.cannon_icon_dx = CANNON_ICON_X_SPEED
        self.cannon_icon_dy = CANNON_ICON_Y_SPEED

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
            self.cannon_base.x = mouse.x - self.cannon_base.width/2
            self.cannon_tube.x = mouse.x - self.cannon_tube.width/2
            self.outer_flame.x = mouse.x - self.outer_flame.width / 2
            self.inner_flame_1.x = mouse.x - self.inner_flame_1.width / 2
            self.inner_flame_2.x = mouse.x - self.inner_flame_2.width / 2

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
