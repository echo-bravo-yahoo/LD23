#wrap to 80, you idiot.
from WIP import *
world1 = World()

#if you do need the index
#for i, elem in enumerate(['a', 'b']):
#print i
#print elem

#import and initialize curses
import curses
global stdscr
stdscr = curses.initscr()
stdscr.keypad(1)
curses.nocbreak()
curses.echo()

def inputParse():
    """Redraw the curses screen and get user input, returned as a string."""

    while(True):
        stdscr.addstr(curses.LINES-1, 0, ">")
        c = ''
        c = stdscr.getstr()
        stdscr.clear()
        stdscr.refresh()        
        return c

stdscr.addstr(0, 0, "Hello. You don't wake up; you come to.\nThat's an important distinction to you.\nYou should look around. You remember\nthat \"look\" is bound to \"December.\"\n")
while(True):
    try:
        stdscr.addstr(0, 0, world1.player1.act(inputParse()))
    #except curses.error:
        #pass
    except Exception as e:
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        exit("Oops! We broke something.")
        raise e