"""
File: center_me.py
Name: Jerry Liao 2020/05
--------------------------------
This program shows how to center a GRect
on windows where the width and the height are
randomly chosen
"""

from campy.graphics.gobjects import GRect, GPolygon, G3DRect
from campy.graphics.gwindow import GWindow

# It controls the width and height of the rect
SIZE = 100
window = GＷindow()

def main():
    """
    Center a magenta rect on the canvas
    where the width and height are SIZE
    """
    # rect = GRect(SIZE, SIZE)
    # rect.filled = True
    # rect.color = 'magenta'
    # rect.fill_color = 'magenta'
    # window = GWindow()
    # rect_x = (window.width-rect.width)/2
    # rect_y = (window.height-rect.height)/2
    # window.add(rect, rect_x, rect_y)
    # parallelogram = GPolygon()
    # parallelogram.add_vertex((50, 50))
    # parallelogram.add_vertex((100, 100))
    # parallelogram.add_vertex((100, 80))
    # parallelogram.add_vertex((50, 30))
    # window.add(parallelogram, 100, 300)
    test = G3DRect(50, 50, x = 100, y = 100, raised = False)
    window.add(test, 100, 300)








if __name__ == '__main__':
    main()
