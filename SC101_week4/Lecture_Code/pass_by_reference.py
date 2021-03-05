"""
File: pass_by_reference.py
Name: Jerry Liao
-------------------------------
This program demonstrates the concept of 
pass-by-reference by showing the color change 
of GRect.
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow

window = GWindow()


def main():
	rect = GRect(100, 100)
	rect.filled = True
	rect.fill_color = 'green'
	window.add(rect, 0, 0)
	change_color(rect)


def change_color(rect):
	rect.fill_color = 'magenta'


if __name__ == '__main__':
	main()
