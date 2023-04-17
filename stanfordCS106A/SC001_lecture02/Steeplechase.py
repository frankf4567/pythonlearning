"""
File: Steeplechase.py
Name: william:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *



def main():
   for i in range(11):
    if front_is_clear():
        move()
    else:
        jump()



def jump():
    """
    pre-condition:karel is on the left,facing east
    post-condition:karel is on the right
    """
    up()
    turn_left()
    turn_left()
    turn_left()
    move()
    down()



def up():
    """
        pre-condition:karel is on the left,facing east
        post-condition:karel is on the top,facing north
    """
    turn_left()
    while not right_is_clear():
        move()



def down():
    """
    pre-condition:karel is on the top,facing east
    post-condition:karel is on the right,facing east
    :return:
    """
    turn_left()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
