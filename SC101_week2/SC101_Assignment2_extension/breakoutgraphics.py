"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Bricks Breakout Game!
Three lives and let's see how good you are!
Extension with larger balls, extra lives and weaponize features

author: sheng-hao wu
description: class/object/method defined file
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 10         # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 120           # Width of a brick (in pixels).
BRICK_HEIGHT = 40          # Height of a brick (in pixels).
BRICK_ROWS = 5             # Number of rows of bricks.
BRICK_COLS = 10            # Number of columns of bricks.
BRICK_OFFSET = 50          # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 20           # Radius of the ball (in pixels).
PADDLE_WIDTH = 200         # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15         # Height of the paddle (in pixels).
PADDLE_OFFSET = 50         # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 4.0      # Initial vertical speed for the ball.
MAX_X_SPEED = 4            # Maximum initial horizontal speed for the ball.
MIN_X_SPEED = 2            # Minimum initial horizontal speed for the ball.
NUM_LIVES   = 3            # Number of lives
CANNON_BASE_WIDTH = 30     # Width of cannon base
CANNON_BASE_HEIGHT = 8     # Height of cannon base
CANNON_TUBE_WIDTH = 10     # Width of cannon tube
CANNON_TUBE_HEIGHT = 20    # Height of cannon tube
MAX_CANNON_BRICKS = 35     # Maximum remained bricks to trigger cannon
MIN_CANNON_BRICKS = 30     # Minimum remained bricks to trigger cannon
OUTER_FLAME_WIDTH = 30     # Width of outer flame
INNER_FLAME1_WIDTH = 20    # Width of inner flame
INNER_FLAME2_WIDTH = 15    # Width of inner flame
PROPERTY_ICON_Y_SPEED = 2  # Cannon icon y speed
PROPERTY_ICON_X_SPEED = 0  # Cannon icon x speed
BALL_RADIUS_INCREASE = 10  # Ball Increase Size
BALL_INCREASE_INTERVAL = 4 # Ball increase appearance interval
LIFE_INCREASE_INTERVAL = 3 # Life increase appearance interval


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

        # Score label
        self.score = 0
        self.score_label = GLabel("Score: " + str(self.score), 100, 200)
        self.score_label.font = "monospace-30-bold"
        self.window.add(self.score_label, 10, self.window.height - 10)

        # life icon
        self.num_lives = NUM_LIVES
        self.life_icons = {}
        for i in range(self.num_lives):
            self.life_icons[i] = GImage("heart_icon.jpeg")
            self.window.add(self.life_icons[i], self.window.width - ( self.life_icons[i].width * (i + 1)), self.window.height - self.life_icons[i].height - 12)

        # Default initial velocity and direction control for the ball.
        self.init_ball_velocity()

        # Game flow control related
        self.ball_active = False
        self.ball_destroy = False
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
        self.bricks_rows = brick_rows
        self.bricks_spacing = brick_spacing
        self.bricks_height = brick_height

        # Gave over label
        self.over_label = GLabel("Game Over")
        self.over_label.color = "red"
        self.over_label.font = "italic-100-bold"

        # create paddle cannon.
        self.cannon_base = GRect(CANNON_BASE_WIDTH, CANNON_BASE_HEIGHT, x=(window_width - CANNON_BASE_WIDTH) / 2, y=window_height - paddle_height - paddle_offset - CANNON_BASE_HEIGHT)
        self.obj_fill_color_add(self.cannon_base, "black", False)
        self.cannon_tube = GRect(CANNON_TUBE_WIDTH, CANNON_TUBE_HEIGHT, x=(window_width - CANNON_TUBE_WIDTH) / 2, y=window_height - paddle_height - paddle_offset - CANNON_BASE_HEIGHT - CANNON_TUBE_HEIGHT)
        self.obj_fill_color_add(self.cannon_tube, "black", False)

        # create cannon flame related instance variables
        self.outer_flame = GRect(OUTER_FLAME_WIDTH, self.cannon_tube.y, x=(window_width - OUTER_FLAME_WIDTH) / 2, y=0)
        self.obj_fill_color_add(self.outer_flame, "red", False)
        self.inner_flame_1 = GRect(INNER_FLAME1_WIDTH, self.cannon_tube.y, x=(window_width - INNER_FLAME1_WIDTH) / 2, y=0)
        self.obj_fill_color_add(self.inner_flame_1, "yellow", False)
        self.inner_flame_2 = GRect(INNER_FLAME2_WIDTH, self.cannon_tube.y, x=(window_width - INNER_FLAME2_WIDTH) / 2, y=0)
        self.obj_fill_color_add(self.inner_flame_2, "lightyellow", False)
        self.flame_appear = False

        # create cannon related instance variables
        self.cannon_appear = False
        self.cannon_icon = GImage("cannon_icon.jpeg")
        self.cannon_icon_background = GRect(self.cannon_icon.width, self.cannon_icon.height)
        self.obj_fill_color_add(self.cannon_icon, "black", False)
        self.cannon_icon_dx = PROPERTY_ICON_X_SPEED
        self.cannon_icon_dy = PROPERTY_ICON_Y_SPEED
        self.trigger_cannon_bricks_num = random.randint(MIN_CANNON_BRICKS, MAX_CANNON_BRICKS)

        # create ball size increase related instance variables
        self.ball_size_inc_appear = False
        self.ball_size_inc_icon = GImage("ball_size_inc.jpeg")
        self.ball_size_inc_icon_background = GRect(self.ball_size_inc_icon.width, self.ball_size_inc_icon.height)
        self.obj_fill_color_add(self.ball_size_inc_icon, "black", False)
        self.ball_size_inc_icon_dx = PROPERTY_ICON_X_SPEED
        self.ball_size_inc_icon_dy = PROPERTY_ICON_Y_SPEED
        self.ball_inc_appearance_interval = BALL_INCREASE_INTERVAL
        self.trigger_ball_size_inc_bricks_num = random.randint(BRICK_ROWS * BRICK_COLS - self.ball_inc_appearance_interval, BRICK_ROWS * BRICK_COLS)
        self.ball_increase = False
        self.ball_radius_increase = BALL_RADIUS_INCREASE

        # create life icon related instance variables
        self.life_inc_appear = False
        self.life_icon = GImage("heart_icon.jpeg")
        self.life_inc_background = GRect(self.life_icon.width, self.life_icon.height)
        self.obj_fill_color_add(self.life_inc_background, "white", False)
        self.life_inc_icon_dx = PROPERTY_ICON_X_SPEED
        self.life_inc_icon_dy = PROPERTY_ICON_Y_SPEED
        self.life_inc_appearance_interval = LIFE_INCREASE_INTERVAL
        self.trigger_life_inc_bricks_num = random.randint(BRICK_ROWS * BRICK_COLS - self.life_inc_appearance_interval, BRICK_ROWS * BRICK_COLS)
        self.life_increase = False



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

    def init_ball_velocity(self):
        self.__dx = random.randint(MIN_X_SPEED, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

        if self.__dx > 0:
            self.__dx_right = True
        else:
            self.__dx_right = False

        self.__dy = INITIAL_Y_SPEED
        self.__dy_down = True

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
    def obj_fill_color_add(self, obj, color, add = True):
        obj.color = color
        obj.filled = True
        obj.fill_color = color
        if add:
            self.window.add(obj)
