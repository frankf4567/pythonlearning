"""
File: PotholeFilling.py
Name: william:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
def put_99_beepers():
    for i in range(99):
        put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()

def go_in():
    """
    pre-condition:karel is at the upper left of the pothole,facing rast
    post-condition:karel is at the pothole,facing south
    """
    move()
    turn_right()
    move()



def go_out():
    """
    pre-condition:karel is at the pothole,facing south
    post-condition:karel is at the upper left of the pothole,facing rast
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()




 # ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
