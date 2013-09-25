#!/usr/bin/env python3
import curses
import time
import subprocess
import sys

import getch
import terminal

from multiprocessing import Process

print(terminal.width)
print(terminal.height)

version = "0.1(beta)"
author = ["Timo Dekker","Dion Bosschieter"]
global win
global name

def sayName():
    name = input("What is your name: ")
    #subprocess.call(["/usr/bin/say", "Welcome " + name])

def drawWindow():
    global stdscr
    stdscr = curses.initscr()
    win = curses.newwin(0,0,0,0)
    # Add the Border
    win.border(0)
    # Current text: Progress
    title = "Network Monitor - "
    title += author[0] + " " + author[1]
    title += " Version: " + version
    win.addstr(0,1,title)
    win.refresh()
    
def drawName():
    win.addstr(2,1,name)

def keyboardInterrupt():
    time.sleep(1)
    while(True):
        c = getch.getch()
        if c == 's': drawName()
        elif c == 'q': exitSystem()
        #elif c == curses.KEY_HOME: x = y = 0

def exitSystem():
    curses.endwin()
    print("Exiting 123...")
    sys.exit(0)

if __name__ == '__main__':
    sayName()
    drawWindow()
    #p = Process(target=keyboardInterrupt)
    #p.start()
    keyboardInterrupt()