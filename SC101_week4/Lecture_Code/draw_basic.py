#!/usr/bin/env python3

"""
Stanford CS106AP
TK Drawing Lecture Exercises
Courtesy of Nick Parlante
"""
import tkinter as tk


# provided function, this code is complete
def make_canvas(width, height):
    """
    Creates and returns a drawing canvas
    of the given int size, ready for drawing.
    """
    top = tk.Tk()
    top.minsize(width=width + 10, height=height + 10)

    canvas = tk.Canvas(top, width=width, height=height)
    canvas.pack()
    canvas.xview_scroll(6, "units")  # hack so (0, 0) works correctly
    canvas.yview_scroll(6, "units")

    return canvas


def main():
    w = make_canvas(500, 300)
    # draw line
    # w.create_line(x1, y1, x2, y2, width = X, fill = "X"
    w.create_line(0, 200, 200, 200, width = 10, fill = "blue")
    #create text
    w.create_text(0, 0, text = "Hello World!", anchor = tk.NW, fill = "red", font = 'times, 40')
    # anchor can change the text
    #tk.NW / tk.NE / tk.SW / tk.SE
    tk.mainloop()

    

if __name__ == '__main__':
    main()
