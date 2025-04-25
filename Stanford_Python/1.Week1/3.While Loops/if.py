'''
File: stanfordkarel.py
-------------------------------------------------------------------
This file for teaching purposes.
-------------------------------------------------------------------
if else code This is a worked example. Karel will "invert" each beeper 
in the first row. To invert a beeper: if there was a beeper
pick it up. Otherwise, put one down.

Author: Shan 
'''

from stanfordkarel import *

def main():
    while front_is_clear():
        invert_beeper()
        move()
    invert_beeper()



def invert_beeper():
    if beepers_present():
        pickup_beeper()
    else:
        put_beeper()
        
if __name__ == '__main__':
    run_karel_program()