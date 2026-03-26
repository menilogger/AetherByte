from time import sleep
from math import floor, ceil
from pyautogui import position, moveTo, click, press, Point
import keyboard as kb
from random import random

def get_position():
    kb.wait('`')
    return position()

def random_point(p1: Point, p2: Point) -> Point:
   # Get Mimimum x and y points
    if p1.x > p2.x:
       x_min = p2.x
       x_max = p1.x
    else:
       x_min = p1.x
       x_max = p2.x
    
    if p1.y > p2.y:
        y_min = p2.y
        y_max = p1.y
    else:
        y_min = p1.y
        y_max = p2.y
    # Get random point from range of x and y
    rand = random()
    x = floor(x_min + (x_max - x_min) * rand)
    y = floor(y_min + (y_max - y_min) * rand)

    return Point(x,y)

def action(actionName: str, loc: Point = None, duration: int = None, key: str = None, wait = 0.2):
    if actionName == 'move' and loc != None:
        moveTo(loc.x, loc.y, duration)
    elif actionName == 'clickRight':
        click(button='right')
    elif actionName == 'click':
        click()
    elif actionName == 'press':
        press(key)
    sleep(wait)

def __main__():
    # Get Bank Points
    bank_p1 = get_position()
    bank_p2 = get_position()
    bank = random_point(bank_p1, bank_p2)

    # Menu position
    menu = Point(bank.x, bank.y + 60)

    # Get Well Points
    well_p1 = get_position()
    well_p2 = get_position()
    well = random_point(well_p1,well_p2)

    # Get how many items need to be done
    inventories = ceil(1000/14)

    for _ in range(inventories):
        action('move', bank, 0.5)

        action('clickRight')

        action('move', menu, 0.2)

        action('click')

        action('move', well, 0.2)

        action('click',wait=1.3)

        action('press', key='space', wait=18)
