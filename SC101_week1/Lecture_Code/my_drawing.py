"""
File: my_drawing.py
Name: 
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause


def main():
    # window = GWindow(width = 1000, height = 800, title = 'MyFacew')
    # face = GOval(250, 350, x = 350 , y = 200)
    # face.filled = True
    # face.fill_color = 'lightpink'
    # window.add(face)
    # l_eye = GOval(50, 50, x = 400, y = 250)
    # l_eye.filled = True
    # l_eye.fill_color = 'black'
    # window.add(l_eye)
    # r_eye = GOval(50, 50, x = 500, y = 250)
    # r_eye.filled = True
    # r_eye.fill_color = 'black'
    # window.add(r_eye)
    # mouth = GRect(150, 50, x = 400, y = 400)
    # mouth.filled = True
    # mouth.fill_color = 'red'
    # window.add(mouth)
    # window.draw_oval(50, 50, 500, 200)
    #
    # label = GLabel('Hello World!', 100, 200)
    # label.color = 'magenta'
    # window.add(label, 100, 200)
    window = GWindow()
    # triangle = GPolygon()
    # triangle.add_vertex((100, 200))
    # triangle.add_vertex((200, 200))
    # triangle.add_vertex((150, 100))
    # triangle.filled = True
    # triangle.fill_color = 'blue'
    # window.add(triangle)
    arc = GArc(200, 80, 0, 180, window.width/2, window.height/2)
    arc.filled = True
    arc.fill_color = 'red'
    window.add(arc)




if __name__ == '__main__':
    main()
