"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect, GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.mouse import onmousedragged

# This constant controls the size of the GRect
SIZE = 100
window = GWindow()
rect = GRect(SIZE, SIZE)

def main():
	window.add(rect)
	rect.filled = True
	rect.fill_color = 'blue'
	# onmousedragged(draw)
	onmousemoved(reset_position)
	# onmouseclicked(function)

def reset_position(event):
	rect.x = event.x - rect.width/2
	rect.y = event.y - rect.height/2
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

if __name__ == '__main__':
	main()
