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
        moveTo(bank.x,bank.y,0.5)
        sleep(0.2)
        click(button="right")
        sleep(0.2)
        moveTo(menu.x,menu.y,0.2)
        sleep(0.2)
        click()
        sleep(0.2)
        moveTo(well.x,well.y)
        sleep(0.2)
        click()
        sleep(1.3)
        press('space')
        sleep(18)
