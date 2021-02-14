"""
File: draw_line
Name: sheng-hao.wu
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# Constant control the diameter of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

#Constant of circle size
CIRCLE_SIZE = 10

# Global variables
window = GWindow(width = WINDOW_WIDTH, height = WINDOW_HEIGHT, title = "draw_line")

#for painter function usage
counter = 0
circle_point = (None)

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(painter)

def painter(mouse):
    global counter, circle_point
    #on odd click, create circle on current location
    if counter is 0:
        circle = GOval(CIRCLE_SIZE, CIRCLE_SIZE, x=mouse.x - CIRCLE_SIZE / 2, y=mouse.y - CIRCLE_SIZE / 2)
        circle.filled = False
        #record current circle location
        circle_point = (circle.x + circle.width/2, circle.y + circle.height/2)
        window.add(circle)
        # increase counter to one in odd clicks
        counter+=1
    #on even click, draw line and remove circle
    else:
        #remove previous circle
        window.remove(window.get_object_at(circle_point[0], circle_point[1]))

        #draw a line from previous circle center to current mouse location
        line = GLine(circle_point[0], circle_point[1], mouse.x, mouse.y)
        window.add(line)
        #decrease counter to zero in even clicks
        counter-=1

if __name__ == "__main__":
    main()
