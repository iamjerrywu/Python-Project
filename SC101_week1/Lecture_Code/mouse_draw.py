"""
File: mouse_draw.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousedragged

# This constant controls the size of the pen stroke
SIZE = 30
window = GWindow()


def main():
	onmousedragged(draw)

def draw(mouse):
	stroke = GOval(SIZE, SIZE, x = mouse.x-SIZE/2, y = mouse.y-SIZE/2)
	stroke.filled = True
	if mouse.x >= window.width/2:
		stroke.color = 'red'
		stroke.fill_color = 'red'
	else:
		stroke.color = 'blue'
		stroke.fill_color = 'blue'
	window.add(stroke)


if __name__ == '__main__':
	main()
