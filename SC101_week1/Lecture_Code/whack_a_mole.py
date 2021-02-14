"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel, GRect
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random
from campy.graphics.gimage import GImage

# Constants control the diameter of the window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700

# Constant controls the pause time of the animation
DELAY = 550

# Global variables
window = GWindow(width = WINDOW_WIDTH, height = WINDOW_HEIGHT, title = "whack_a_mole")
score = 0
label = GLabel("Score: " + str(score), 100, 200)

def main():
    while True:
        global score
        label.font = '-30'
        label.color = 'Black'
        window.add(label, 0, 50)
        img = GImage('mole.jpeg')
        random_x = random.randint(0, window.width - img.width)
        random_y = random.randint(0, window.height - img.height)
        window.add(img, random_x, random_y)
        pause(DELAY)
        onmouseclicked(function)

def function(mouse):
    global score
    maybe_object = window.get_object_at(mouse.x,mouse.y)
    if (maybe_object is not None and maybe_object is not label):
        window.remove(maybe_object)
        score+=1
        label.text = "Score: " + str(score)




if __name__ == '__main__':
    main()
