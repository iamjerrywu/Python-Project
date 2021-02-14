from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ZONE_WIDTH = 350
ZONE_HEIGHT = 300
BALL_RADIUS = 15
MAX_SPEED = random.randint(5, 10)
MIN_SPEED = random.randint(1, 5)


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='ZONE_GAME')
        # Create zone
        self.zone = GRect(zone_width, zone_height, x = (self.window.width - zone_width)/2, y = (self.window.height - zone_height)/2)
        self.zone.color = 'blue'
        self.zone.filled = True
        self.zone.fill_color = "blue"
        self.window.add(self.zone)
        # Create ball and initialize velocity/position
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.set_ball_position()
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        #speed
        self.dx_right = True
        self.dy_down = True
        #bounce

        # Initialize mouse listeners


    def set_ball_position(self):
        while True:
            rand_x = random.randint(0, self.window.width - self.ball.width)
            rand_y = random.randint(0, self.window.height - self.ball.height)
            if not (self.zone.x < rand_x < self.zone.x + ZONE_WIDTH and self.zone.y < rand_y < self.zone.y + ZONE_HEIGHT):
                break
        self.ball.x = rand_x
        self.ball.y = rand_y

    def set_ball_velocity(self):
        self.dx = random.randint(MIN_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.dx*= -1
        self.dy = random.randint(MIN_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.dy*= -1