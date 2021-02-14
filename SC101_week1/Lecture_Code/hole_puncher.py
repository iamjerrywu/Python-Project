"""
File: hole_puncher.py
Name:
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause

# This constant controls the size of the hole
SIZE = 30
window = GWindow()

def main():
        for i in range(10):
            onmouseclicked(function)
            print("shit")
            pause(100)

def function(mouse):
    oval = GOval(SIZE, SIZE, x = mouse.x - SIZE/2, y = mouse.y - SIZE/2)
    oval.filled = True
    oval.fill_color = 'black'
    window.add(oval)

if __name__ == '__main__':
    main()
