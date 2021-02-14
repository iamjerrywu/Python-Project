"""
File: my_drawing.py
Name: sheng-hao.wu

Description: batman standing insides of his house while somebody call for help, illuminating batman icon in night sky
----------------------
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine, GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.timer import pause

# Constant control the diameter of the window
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 900

#Constant for init position (invalid while x = -100, y = -100)
INIT_POSITION = (-100, -100)
# Global variables
window = GWindow(width = WINDOW_WIDTH, height = WINDOW_HEIGHT, title = "bat_man_and_logo_light")

#function help fill object color
def obj_fill_color_add(obj, color):
    obj.filled = True
    obj.fill_color = color
    window.add(obj)

#function help create polygon, require at least 3 points for triangle, and support up to six points (hexagon)
def polygon_helper(obj, color, point1, point2, point3, point4 = INIT_POSITION, point5 = INIT_POSITION, point6 = INIT_POSITION):
    obj.add_vertex(point1)
    obj.add_vertex(point2)
    obj.add_vertex(point3)
    if point4 is not INIT_POSITION:
        obj.add_vertex(point4)
    if point5 is not INIT_POSITION:
        obj.add_vertex(point5)
    if point6 is not INIT_POSITION:
        obj.add_vertex(point6)
    obj_fill_color_add(obj, color)

#function help design font
def label_helper(obj, color, font_style, x, y):
    obj.color = color
    obj.font = font_style
    window.add(obj, x, y)

#create objects in batman's house
def house_background():
    night_sky = GRect(WINDOW_WIDTH, WINDOW_HEIGHT)
    obj_fill_color_add(night_sky, "darkgrey")
    house_obj = [None] * 3
    # room floor
    house_obj[0] = GPolygon()
    polygon_helper(house_obj[0], "oldlace", (300, 750), (1500, 750), (1500, 900), (  0, 900))
    # left wall
    house_obj[1] = GPolygon()
    polygon_helper(house_obj[1], "oldlace", (  0, -20), ( 300,  50), ( 300, 750), (  0, 900))
    # ceiling
    house_obj[2] = GPolygon()
    polygon_helper(house_obj[2], "oldlace", (  0, -20), (1500,   0), (1500,  50), (300,  50))

# create objects in the night view outside the window of batman house
def night_view():
    # total 12 buildings
    building = [None] * 12

    #total 10 windows
    windows_position = [[350, 550], [525, 450], [525, 550], [650, 650], [725, 500], [850, 400], [850, 450], [950, 600],
                        [1350, 600], [1450, 500]]
    building_window = [None] * len(windows_position)

    # start creating buildings in night view
    building[0] = GPolygon()
    polygon_helper(building[0], "black", (300, 500), (300, 750), (400, 750), (400, 500))
    building[1] = GPolygon()
    polygon_helper(building[1], "black", (400, 600), (400, 750), (500, 750), (500, 400))
    building[2] = GPolygon()
    polygon_helper(building[2], "black", (500, 400), (400, 750), (600, 750), (600, 400))
    building[3] = GPolygon()
    polygon_helper(building[3], "black", (600, 600), (400, 750), (700, 750), (700, 600))
    building[4] = GPolygon()
    polygon_helper(building[4], "black", (700, 450), (700, 750), (800, 750), (800, 450))
    building[5] = GPolygon()
    polygon_helper(building[5], "black", (800, 350), (800, 750), (900, 750), (900, 350), (850, 300))
    building[6] = GPolygon()
    polygon_helper(building[6], "black", (900, 550), (900, 750), (1000, 750), (1000, 550))
    building[7] = GPolygon()
    polygon_helper(building[7], "black", (1000, 600), (1000, 750), (1100, 750), (1100, 600))
    building[8] = GPolygon()
    polygon_helper(building[8], "black", (1100, 650), (1100, 750), (1200, 750), (1200, 650))
    building[9] = GPolygon()
    polygon_helper(building[9], "black", (1200, 600), (1200, 750), (1300, 750), (1300, 650))
    building[10] = GPolygon()
    polygon_helper(building[10], "black", (1300, 525), (1300, 750), (1400, 750), (1400, 525))
    building[11] = GPolygon()
    polygon_helper(building[11], "black", (1400, 450), (1400, 750), (1500, 750), (1500, 450))

    #start creating windows in night view
    for i in range(len(windows_position)):
        building_window[i] = GRect(20, 20, x = windows_position[i][0], y = windows_position[i][1])
        obj_fill_color_add(building_window[i], "silver")

# create batman details
def batman():
    #batman legs
    left_leg = GRect(40, 100, x = 280, y = 775)
    obj_fill_color_add(left_leg, "gray")
    left_shoe = GPolygon()
    polygon_helper(left_shoe, "dimgrey", (280, 840), (280, 880), (330, 880), (320, 840))
    right_leg = GRect(40, 100, x = 360, y = 775)
    obj_fill_color_add(right_leg, "gray")
    right_shoe = GPolygon()
    polygon_helper(right_shoe, "dimgrey", (360, 840), (360, 880), (410, 880), (400, 840))

    #batman head
    bat_ear1 = GPolygon()
    polygon_helper(bat_ear1, "gray", (275, 450), (325, 450), (300, 375))
    head = GOval(180, 220, x = 260, y = 400)
    obj_fill_color_add(head, "gray")
    bat_ear2 = GPolygon()
    polygon_helper(bat_ear2, "gray", (360, 450), (410, 450), (385, 375))

    #batman appearance
    face = GArc(275, 330, 0, -90, 300, 450)
    obj_fill_color_add(face, "bisque")
    eye = GRect(30, 10, x = 400, y = 475)
    obj_fill_color_add(eye, "white")
    mouth = GLine(405, 575, 425, 575)
    obj_fill_color_add(mouth, "black")

    #batman body
    left_arm = GPolygon()
    polygon_helper(left_arm, "gray", (275, 600), (210, 650), (275, 720), (300, 720), (250, 655), (340, 600))
    right_arm = GPolygon()
    polygon_helper(right_arm, "gray", (355, 600), (415, 650), (385, 720), (405, 720), (455, 650), (405, 600))
    cape = GPolygon()
    polygon_helper(cape, "dimgrey", (280, 580), (250, 800), (450, 800), (380, 580))

#create logo light beam details
def rescue_light():
    #color database
    light_color = ["dimgrey", "lightgrey", "gainsboro", "whitesmoke"]

    light_beam = GPolygon()
    light_beam.color = "darkgrey"
    polygon_helper(light_beam, "darkgrey", (920, 350), (1300, 650), (1255, 250))
    bat_icon_background = GOval(385, 300, x = 870, y = 100)
    bat_icon_background.color = "darkgrey"
    obj_fill_color_add(bat_icon_background, "darkgrey")
    # gradually brighten the beam
    pause(1000)
    for s in light_color:
        light_beam.color = s
        light_beam.fill_color = s
        bat_icon_background.color = s
        bat_icon_background.fill_color = s
        pause(800)
    #batman icon in light
    bat_icon = GImage("batman.jpeg")
    window.add(bat_icon, bat_icon_background.x + 60, bat_icon_background.y + 45)

#create slogal label
def slogan():
    # customized delay for showing each sentence
    pause(1000)
    label1 = GLabel("KEEP\nCALM")
    label_helper(label1, "white", "courier-40-bold", 500, 150)
    pause(1000)
    label2 = GLabel("AND")
    label_helper(label2, "white", "courier-30-bold", 520, 180)
    pause(1000)
    label3 = GLabel("CALL")
    label_helper(label3, "white", "courier-40-bold", 500, 220)
    label4 = GLabel("BATMAN")
    label_helper(label4, "white", "courier-40-bold", 480, 260)
    pause(2500)
    label5 = GLabel("OR CALL ")
    label_helper(label5, "white", "courier-30-bold", 380, 325)
    label5 = GLabel("stanCode")
    label_helper(label5, "red", "courier-50-italic", 530, 330)
    pause(1500)
    label6 = GLabel("0983-513-97X\n   2am-6am")
    label_helper(label6, "white", "courier-20-", 475, 375)

def main():
    house_background()
    night_view()
    batman()
    rescue_light()
    slogan()

if __name__ == '__main__':
    main()
