#wrap to 80, you idiot.
from WIP import *
world1 = World()
import sys
import os
os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
def custom_inputParse():
    c = input(">")
    os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
    return c
print("Hello. You don't wake up; you come to.\nThat's an important distinction to you.\nYou should look around. You remember\nthat \"look\" is bound to \"December.\"")
while(True):
    print("\"{}\"".format(world1.player1.act(custom_inputParse()).rstrip()))