"""
File: DoubleBeepers.py
Name:willliam
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    while not on_beeper():
        move()
    double_beepers()
def double_beepers():
    if on_beeper():
        pick_beeper()
        if on_beeper():
            pick_beeper()
        else:
            for i in range(2):
                put_beeper()
            move3()
        if on_beeper():
                pick_beeper()
        else:
            for i in range(4):
                put_beeper()
            move3()
        if on_beeper():
            pick_beeper()
        else:
            for i in range(6):
                put_beeper()
            move3()
        if on_beeper():
            pick_beeper()
        else:
            for i in range(8):
                put_beeper()
            move3()
        if on_beeper():
            pick_beeper()
        else:
            for i in range(10):
                put_beeper()
            move3()
        if on_beeper():
                pick_beeper()
        else:
            for i in range(12):
                put_beeper()
            move3()
        if on_beeper():
                pick_beeper()
        else:
            for i in range(14):
                put_beeper()
            move3()
        if on_beeper():
                pick_beeper()
        else:
            for i in range(16):
                put_beeper()
            move3()
        if on_beeper():
                pick_beeper()
        else:
            for i in range(18):
                put_beeper()
            move3()
        if on_beeper():
                pick_beeper()
        else:
            for i in range(20):
                put_beeper()
            move3()
        #this code can doubled up to 10 beepers
def move3():
    move()
    move()
    move()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
