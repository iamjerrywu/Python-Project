"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Bricks Breakout Game!
Three lives and let's see how good you are!
Extension with larger balls, extra lives and weaponize features

author: sheng-hao wu
description: animations-related file
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gimage import GImage
import random

FRAME_RATE = 1000 / 120 # 120 frames per second.

# func for checking boundary
def boundary_check(obj):
    # ensure ball's is within window and handles it's direction
    if not obj.ball_destroy:
        if obj.ball.x <= 0 and obj.get_ball_dx_right() is False or obj.ball.x + obj.ball.width >= obj.window.width and obj.get_ball_dx_right() is True:
            obj.set_ball_dx(-obj.get_ball_dx())
            obj.set_ball_dx_right(not obj.get_ball_dx_right())
        if obj.ball.y <= 0 and obj.get_ball_dy_down() is False:
            obj.set_ball_dy(-obj.get_ball_dy())
            obj.set_ball_dy_down(True)
        # if ball's out of window's low bound, life count - 1 and pause the game
        elif obj.ball.y >= obj.window.height:
            obj.ball_active = False
            obj.window.remove(obj.life_icons[obj.remained_life - 1])
            obj.life_icons.pop(len(obj.life_icons) - 1)
            obj.remained_life-=1

def collisions_handler(obj):

    # handle ball's collision
    ball_collision_handler(obj)

    # handle if cannon icon touch paddle
    maybe_obj = obj.window.get_object_at(obj.cannon_icon_background.x, obj.cannon_icon_background.y + obj.cannon_icon_background.height + 1)
    if maybe_obj and maybe_obj is obj.paddle:
        obj.window.remove(obj.cannon_icon)
        obj.window.remove(obj.cannon_icon_background)
        create_cannon_flame(obj)

    maybe_obj = obj.window.get_object_at(obj.cannon_icon_background.x + obj.cannon_icon_background.width, obj.cannon_icon_background.y + obj.cannon_icon_background.height + 1)
    if maybe_obj and maybe_obj is obj.paddle:
        obj.window.remove(obj.cannon_icon)
        obj.window.remove(obj.cannon_icon_background)
        create_cannon_flame(obj)

    # handle if ball_size_inc icon touch paddle
    maybe_obj = obj.window.get_object_at(obj.ball_size_inc_icon_background.x,
                                         obj.ball_size_inc_icon_background.y + obj.ball_size_inc_icon_background.height + 1)
    if maybe_obj and maybe_obj is obj.paddle:
        obj.window.remove(obj.ball_size_inc_icon)
        obj.window.remove(obj.ball_size_inc_icon_background)
        obj.ball_size_inc_appear = False
        obj.trigger_ball_size_inc_bricks_num = random.randint(obj.remained_bricks - obj.ball_inc_appearance_interval, obj.remained_bricks)
        if not obj.ball_increase:
            obj.ball_increase = True
            obj.ball._height+=obj.ball_radius_increase
            obj.ball._width+=obj.ball_radius_increase
            obj.window.remove(obj.ball)
            obj.obj_fill_color_add(obj.ball, "black")

    maybe_obj = obj.window.get_object_at(obj.ball_size_inc_icon_background.x + obj.ball_size_inc_icon_background.width, obj.ball_size_inc_icon_background.y + obj.ball_size_inc_icon_background.height + 1)
    if maybe_obj and maybe_obj is obj.paddle:
        obj.window.remove(obj.ball_size_inc_icon)
        obj.window.remove(obj.ball_size_inc_icon_background)
        obj.ball_size_inc_appear = False
        obj.trigger_ball_size_inc_bricks_num = random.randint(obj.remained_bricks - obj.ball_inc_appearance_interval, obj.remained_bricks)
        if not obj.ball_increase:
            obj.ball_increase = True
            obj.ball._height += obj.ball_radius_increase
            obj.ball._width += obj.ball_radius_increase
            obj.window.remove(obj.ball)
            obj.obj_fill_color_add(obj.ball, "black")

    # handle if ball_size_inc_icon out of bound (user miss and need to regenerate chance)
    if obj.ball_size_inc_icon and obj.ball_size_inc_icon_background:
        if obj.ball_size_inc_icon.y > obj.window.height and obj.ball_size_inc_icon_background.y > obj.window.height:
            obj.window.remove(obj.ball_size_inc_icon)
            obj.window.remove(obj.ball_size_inc_icon_background)
            obj.ball_size_inc_appear = False
            obj.trigger_ball_size_inc_bricks_num = random.randint(
            obj.remained_bricks - obj.ball_inc_appearance_interval, obj.remained_bricks)

    # handle flame collide with bricks
    if obj.flame_appear:
        not_rm_list = [obj.ball_size_inc_icon, obj.ball_size_inc_icon_background, obj.life_icon, obj.life_inc_background]
        for i in range(obj.bricks_rows):
            # only need to take care outer flame
            rm_obj = obj.window.get_object_at(obj.outer_flame.x - 1, obj.outer_flame.y + (i + 1) * (obj.bricks_spacing + obj.bricks_height) - obj.bricks_height/2)
            if rm_obj and rm_obj not in not_rm_list:
                rm_obj_handler(rm_obj, obj)
            rm_obj = obj.window.get_object_at(obj.outer_flame.x + obj.outer_flame.width + 1, obj.outer_flame.y + (i + 1) * (obj.bricks_spacing + obj.bricks_height) - obj.bricks_height / 2)
            if rm_obj and rm_obj not in not_rm_list:
                rm_obj_handler(rm_obj, obj)


# remove object
def rm_obj_handler(rm_obj, obj):
    # if ball touch these objs, don't remove that obj
    not_rm_obj_list = [obj.paddle, obj.cannon_base, obj.cannon_tube, obj.life_icon, obj.life_inc_background]
    # if ball touch these objs, remove ball itself
    rm_ball_list = [obj.outer_flame, obj.inner_flame_1, obj.inner_flame_2]
    if rm_obj in rm_ball_list:
        obj.window.remove(obj.ball)
        obj.ball_destroy = True
    elif rm_obj is obj.life_icon:
        new_life_index = len(obj.life_icons)
        obj.life_icons[new_life_index] = GImage("heart_icon.jpeg")
        obj.window.add(obj.life_icons[new_life_index], obj.window.width - (obj.life_icons[new_life_index].width * (new_life_index + 1)), obj.window.height - obj.life_icons[new_life_index].height - 12)

        obj.remained_life+=1
        obj.window.remove(rm_obj)
        obj.life_inc_appear = False
        obj.life_increase = True

    elif rm_obj not in not_rm_obj_list:
        # create color-score map
        color_score_map = {"midnightblue":50, "mediumblue":40, "blue":30, "dodgerblue":20, "lightskyblue":10}

        # update score
        obj.score+=color_score_map[rm_obj.color_str]
        obj.score_label.text = "Score: " + str(obj.score)

        # if hit brick with cannon icon property, create cannon icon
        if not obj.cannon_appear and obj.remained_bricks <= obj.trigger_cannon_bricks_num:
            if obj.remained_bricks != obj.trigger_ball_size_inc_bricks_num or obj.remained_bricks != obj.trigger_life_inc_bricks_num:
                create_cannon_icon(obj, rm_obj)
        if not obj.ball_size_inc_appear and obj.remained_bricks <= obj.trigger_ball_size_inc_bricks_num:
            if obj.remained_bricks != obj.trigger_cannon_bricks_num or obj.remained_bricks != obj.trigger_life_inc_bricks_num:
                create_ball_size_inc_icon(obj, rm_obj)
        if not obj.life_inc_appear and obj.remained_bricks <= obj.trigger_life_inc_bricks_num:
            if obj.remained_bricks != obj.trigger_cannon_bricks_num or obj.remained_bricks != obj.trigger_ball_size_inc_bricks_num:
                create_life_inc_icon(obj, rm_obj)
        # create color-score map
        color_score_map = {"midnightblue":50, "mediumblue":40, "blue":30, "dodgerblue":20, "lightskyblue":10}

        # update score
        obj.score+=color_score_map[rm_obj.color_str]
        obj.score_label.text = "Score: " + str(obj.score)

        # remove bricks
        obj.window.remove(rm_obj)
        obj.remained_bricks-=1


def ball_collision_handler(obj):
    change_dx = False
    change_dy = False

    """
    algorithm for handling collision:
        1. identify whether hit object in ball's four vertices respectively
            a. if yes, then identify the ball's relevant position to the object that it collides
                i. calculate the ball's previous position before collide, prev_pos(x,y) = cur_pos(x +/- abs(dx), y+/- abs(dy))
            b. based on the relationship between ball's previous position and the collide object, then change ball's direction
    """
    no_collide_list = [obj.score_label, obj.cannon_icon_background, obj.cannon_icon, obj.ball_size_inc_icon_background, obj.ball_size_inc_icon]
    for i in range(len(obj.life_icons)):
        no_collide_list.append(obj.life_icons[i])
    print(len(obj.life_icons))
    if not obj.ball_destroy:
        # upper-left point:
        rm_obj = obj.window.get_object_at(obj.ball.x, obj.ball.y)
        if rm_obj and rm_obj not in no_collide_list:
            if obj.ball.x + abs(obj.get_ball_dx()) > rm_obj.x + rm_obj.width and obj.get_ball_dx_right() is False:
                change_dx = True
            if obj.ball.y + abs(obj.get_ball_dy()) >= rm_obj.y + rm_obj.height and obj.get_ball_dy_down() is False:
                change_dy = True
            # remove object
            rm_obj_handler(rm_obj, obj)

        # down-left point:
        rm_obj = obj.window.get_object_at(obj.ball.x, obj.ball.y + obj.ball.height)
        if rm_obj and rm_obj not in no_collide_list:
            if obj.ball.x + abs(obj.get_ball_dx()) > rm_obj.x + rm_obj.width and obj.get_ball_dx_right() is False:
                change_dx = True
            if obj.ball.y + obj.ball.height - abs(obj.get_ball_dy()) < rm_obj.y and obj.get_ball_dy_down() is True:
                change_dy = True
            # remove object
            rm_obj_handler(rm_obj, obj)

        # down-right point:
        rm_obj = obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y + obj.ball.height)
        if rm_obj and rm_obj not in no_collide_list:
            if obj.ball.x + obj.ball.width - abs(obj.get_ball_dx()) < rm_obj.x and obj.get_ball_dx_right() is True:
                change_dx = True
            if obj.ball.y + obj.ball.height - abs(obj.get_ball_dy()) < rm_obj.y and obj.get_ball_dy_down() is True:
                change_dy = True
            # remove object
            rm_obj_handler(rm_obj, obj)

        # up-right point:
        rm_obj = obj.window.get_object_at(obj.ball.x + obj.ball.width, obj.ball.y)
        if rm_obj and rm_obj not in no_collide_list:
            if obj.ball.x + obj.ball.width - abs(obj.get_ball_dx()) < rm_obj.x and obj.get_ball_dx_right() is True:
                change_dx = True
            if obj.ball.y + abs(obj.get_ball_dy()) >= rm_obj.y + rm_obj.height and obj.get_ball_dy_down() is False:
                change_dy = True
            # remove object
            rm_obj_handler(rm_obj, obj)

        """
        Once the ball get bigger enough need to consider upper / lower middle point, to make it more real
        """
        # if ball is big enough
        if obj.ball.width > obj.paddle.width:
            # down-middle point:
            rm_obj = obj.window.get_object_at(obj.ball.x + obj.ball.width/2, obj.ball.y + obj.ball.height + 1)
            if rm_obj and rm_obj not in no_collide_list:
                if obj.ball.y + obj.ball.height - abs(obj.get_ball_dy()) <= rm_obj.y and obj.get_ball_dy_down() is True:
                    change_dy = True
                # remove object
                rm_obj_handler(rm_obj, obj)
            # up-middle point:
            rm_obj = obj.window.get_object_at(obj.ball.x + obj.ball.width / 2, obj.ball.y - 1)
            if rm_obj and rm_obj not in no_collide_list:
                if obj.ball.y + abs(obj.get_ball_dy()) >= rm_obj.y + rm_obj.height and obj.get_ball_dy_down() is True:
                    change_dy = True
                # remove object
                rm_obj_handler(rm_obj, obj)


        # change ball's direction
        dx = -obj.get_ball_dx() if change_dx is True else obj.get_ball_dx()
        dy = -obj.get_ball_dy() if change_dy is True else obj.get_ball_dy()
        if change_dx or change_dy:
            change_dir_handler(obj, dx, dy)


# func help create cannon icon
def create_cannon_icon(obj, rm_obj):
    obj.cannon_appear = True
    obj.window.add(obj.cannon_icon_background, rm_obj.x + (rm_obj.width - obj.cannon_icon_background.width)/2, rm_obj.y + (rm_obj.height - obj.cannon_icon_background.height)/2)
    obj.window.add(obj.cannon_icon, obj.cannon_icon_background.x, obj.cannon_icon_background.y)


def create_ball_size_inc_icon(obj, rm_obj):
    obj.ball_size_inc_appear = True
    obj.ball_increase = False
    obj.window.add(obj.ball_size_inc_icon_background, rm_obj.x + (rm_obj.width - obj.ball_size_inc_icon_background.width) / 2, rm_obj.y + (rm_obj.height - obj.ball_size_inc_icon_background.height) / 2)
    obj.window.add(obj.ball_size_inc_icon, obj.ball_size_inc_icon_background.x, obj.ball_size_inc_icon_background.y)

def create_life_inc_icon(obj, rm_obj):
    obj.life_inc_appear = True
    obj.life_increase = False
    obj.window.add(obj.life_inc_background, rm_obj.x + (rm_obj.width - obj.life_inc_background.width) / 2, rm_obj.y + (rm_obj.height - obj.life_inc_background.height) / 2)
    obj.window.add(obj.life_icon, obj.life_inc_background.x, obj.life_inc_background.y)


# func help create cannon and flame
def create_cannon_flame(obj):
    obj.flame_appear = True
    obj.window.add(obj.cannon_base, obj.paddle.x + (obj.paddle.width - obj.cannon_base.width)/2, obj.cannon_base.y)
    obj.window.add(obj.cannon_tube, obj.paddle.x + (obj.paddle.width - obj.cannon_tube.width) / 2, obj.cannon_tube.y)
    obj.window.add(obj.outer_flame, obj.paddle.x + (obj.paddle.width - obj.outer_flame.width)/2, obj.outer_flame.y)
    obj.window.add(obj.inner_flame_1, obj.paddle.x + (obj.paddle.width - obj.inner_flame_1.width)/2, obj.inner_flame_1.y)
    obj.window.add(obj.inner_flame_2, obj.paddle.x + (obj.paddle.width - obj.inner_flame_2.width)/2,obj.inner_flame_2.y)


# change ball's direction
def change_dir_handler(obj, dx, dy):
    obj.set_ball_dx(dx)
    obj.set_ball_dy(dy)
    if obj.get_ball_dx() > 0:
        obj.set_ball_dx_right(True)
    else:
        obj.set_ball_dx_right(False)
    if obj.get_ball_dy() > 0:
        obj.set_ball_dy_down(True)
    else:
        obj.set_ball_dy_down(False)


def game_over_handler(obj):
    obj.window.add(obj.over_label, (obj.window.width - obj.over_label.width) / 2, obj.window.height / 2)
    obj.window.remove(obj.paddle)
    obj.window.remove(obj.cannon_base)
    obj.window.remove(obj.cannon_tube)
    obj.window.remove(obj.outer_flame)
    obj.window.remove(obj.inner_flame_1)
    obj.window.remove(obj.inner_flame_2)
    if obj.ball_size_inc_icon and obj.ball_size_inc_icon_background:
        obj.window.remove(obj.ball_size_inc_icon)
        obj.window.remove(obj.ball_size_inc_icon_background)
    if obj.life_icon and obj.life_inc_background:
        obj.window.remove(obj.life_icon)
        obj.window.remove(obj.life_inc_background)


def main():
    graphics = BreakoutGraphics()

    init_dx = abs(graphics.get_ball_dx())
    init_dy = abs(graphics.get_ball_dy())
    acc = [[init_dx + 1, init_dx + 2, init_dx + 3, init_dx + 4], [init_dy + 1, init_dy + 2, init_dy + 3, init_dy + 4]]

    # init remained life
    while True:
        if graphics.ball_active:

            # move ball
            graphics.ball.move(graphics.get_ball_dx(), graphics.get_ball_dy())

            # move cannon/flame
            if graphics.cannon_appear:
                graphics.cannon_icon.move(graphics.cannon_icon_dx, graphics.cannon_icon_dy)
                graphics.cannon_icon_background.move(graphics.cannon_icon_dx, graphics.cannon_icon_dy)
            # move ball_size_inc icon
            if graphics.ball_size_inc_appear:
                graphics.ball_size_inc_icon.move(graphics.cannon_icon_dx, graphics.cannon_icon_dy)
                graphics.ball_size_inc_icon_background.move(graphics.cannon_icon_dx, graphics.cannon_icon_dy)
            # check for collision and handler ball's direction
            collisions_handler(graphics)

            # ball should withinR window boundary, and would end game if it's out of window's low bound
            boundary_check(graphics)
            if not graphics.ball_active:
                if graphics.remained_life == 0:
                    break
                else:
                    graphics.reset_ball_position()
            # if no bricks remaining, gave over
            if graphics.remained_bricks == 0:
                break
            # ball accelerated when game goes on for a while
            if 45 < graphics.remained_bricks <= 47:
                acc_x = acc[0][0] if graphics.get_ball_dx_right() is True else -acc[0][0]
                graphics.set_ball_dx(acc_x)
                acc_y = acc[1][0] if graphics.get_ball_dy_down() is True else -acc[1][0]
                graphics.set_ball_dy(acc_y)
            if 40 < graphics.remained_bricks <= 42:
                acc_x = acc[0][1] if graphics.get_ball_dx_right() is True else -acc[0][1]
                graphics.set_ball_dx(acc_x)
                acc_y = acc[1][1] if graphics.get_ball_dy_down() is True else -acc[1][1]
                graphics.set_ball_dy(acc_y)
            if 35 < graphics.remained_bricks <= 37:
                acc_x = acc[0][2] if graphics.get_ball_dx_right() is True else -acc[0][2]
                graphics.set_ball_dx(acc_x)
                acc_y = acc[1][2] if graphics.get_ball_dy_down() is True else -acc[1][2]
                graphics.set_ball_dy(acc_y)
            if 30 < graphics.remained_bricks <= 32:
                acc_x = acc[0][3] if graphics.get_ball_dx_right() is True else -acc[0][3]
                graphics.set_ball_dx(acc_x)
                acc_y = acc[1][3] if graphics.get_ball_dy_down() is True else -acc[1][3]
                graphics.set_ball_dy(acc_y)

        pause(FRAME_RATE)
    game_over_handler(graphics)


if __name__ == '__main__':
    main()
