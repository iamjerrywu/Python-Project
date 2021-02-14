"""
File: bouncing_rect.py
Name: 
------------------------
This file shows how to make a simple 
animation by campy library
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the width and height of the rect
SIZE = 30

# This controls the pause time (in millisecond) for the animation
DELAY = 10

def set_up_react():
	rect = GRect(SIZE, SIZE, x = (window.width - SIZE)/2, y = (window.height - SIZE)/2 )
	rect.filled = True
	rect.fill_color = 'blue'
	return rect

def main():
	rect = set_up_react()
	window.add(rect, (window.width - rect.width) / 2, (window.height - rect.height) / 2)
	mov_d = 5
	while True:
		if rect.x + mov_d > window.width:
			print("Move Distance out of bound")
			break
		rect.move(mov_d, 0)
		if rect.x <= 0:
			mov_d = -mov_d
			rect.fill_color = 'blue'
		if rect.x + rect.width >= window.width:
			mov_d = -mov_d
			rect.fill_color = 'red'
		pause(10)
			

if __name__ == '__main__':
	window = GWindow()
	main()
