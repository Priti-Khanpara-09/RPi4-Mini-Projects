#This is blueDot control Robot
'''
Write Command on Lx-terminal: sudo pip3 install bluedot
Download The BlueDot Application: https://play.google.com/store/apps/details?id=com.stuffaboutcode.bluedot&hl=en_GB
'''

from bluedot import BlueDot
from gpiozero import Robot
from time import sleep

bd = BlueDot()

robot = Robot(left = (7, 8), right = (9, 10))

def move(pos):
    if pos.top:
        robot.forward()
        sleep(0.1)
    elif pos.bottom:
        robot.backward()
        sleep(0.1)
    elif pos.right:
        robot.right()
        sleep(0.1)
    elif pos.left:
        robot.left()
        sleep(0.1)

def stop():
    robot.stop()
    
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop
