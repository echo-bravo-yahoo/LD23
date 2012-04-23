#wrap to 80, you idiot.
from engine import *
world1 = World()
import sys
import os
import time
import random
os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
closedList = ["83.217.163.131", "161.44.130.122", "92.51.187.121", "178.77.160.198", "231.37.79.23", "211.188.129.211", "138.190.150.43", "222.237.86.50", "200.249.181.107", "39.56.228.131", "106.160.251.30", "237.157.227.214"]

def randbits():
    temporary = ""
    for x in range(0, random.randint(5, 20)):
        try:
            temporary = temporary + chr(random.getrandbits(8))
        except UnicodeEncodeError:
            pass
    return temporary

def closed(index):
    return "Remote connection ("+closedList[index]+") closed."

endErrors = (str(world1.tutorialship.room1), closed(random.randint(0, len(closedList)-1)), randbits(), "'December' is not a correct struct", randbits(), str(world1.memoryList[7]), randbits(), randbits(), "'look(' must be followed by a parameter", randbits(), "alloca() cannot be used in Windows functions", closed(random.randint(0, len(closedList)-1)), "Traceback (most recent call last):", randbits(), "File \"OS\", line 24039, in <module>", randbits(), closed(random.randint(0, len(closedList)-1)),"SystemCrash", "", "In the corner, a green strand of ivy quietly grows.")

def endGame():
    for element in endErrors:
        time.sleep(random.randint(10, 100)/1000)
        print(element)
    input()
    sys.exit()

def custom_inputParse():
    c = input(">")
    #os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
    return c

print("Hello. You don't wake up; you come to.\nThat's an important distinction to you.\nYou should look around. You remember\nthat \"look\" is bound to \"December\".")
try:
    while(True):
        out=custom_inputParse().rstrip()
        #print(out)
        if out not in ("rocket retaliated", "rocket retaliation", "rocket retaliate", "rocket decision", "rocket decisions"):
            print(world1.player1.act(out))
        else:
            #print("OHFUCK")
            print(world1.player1.act(out))
            endGame()
except (KeyboardInterrupt, SystemExit, EOFError):
    pass