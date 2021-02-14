"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect, GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.mouse import onmousedragged
import collections

# This constant controls the size of the GRect
SIZE = 100
window = GWindow()
rect = GRect(SIZE, SIZE)
line = GLine(-1, -1, 100, 100)

def main():
	window.add(line)
	rect.filled = True
	rect.fill_color = 'blue'
	# onmousedragged(draw)
	onmousemoved(reset_position)
	# onmouseclicke®d(function)

def reset_position(event):
	line.x1 = 300
	line.x2 = 200
	line.y1 = 300
	line.y2 = 200
# def draw(mouse):
# 	stroke = GRect(SIZE, SIZE, x = mouse.x-SIZE/2, y = mouse.y-SIZE/2)
# 	stroke.filled = True
# 	stroke.color = 'blue'
# 	stroke.fill_color = 'blue'
# 	window.add(stroke)
#
# def function(mouse):
# 	rect = GRect(SIZE, SIZE, x = mouse.x - SIZE/2, y = mouse.y - SIZE/2)
# 	rect.filled = True
# 	rect.fill_color = 'blue'
# 	window.add(rect)

queue1 = collections deque()

if __name__ == '__main__':
	main()
