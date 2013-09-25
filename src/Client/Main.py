#!/usr/bin/env python3

# Todo:
# Create a class terminal and add a getch method to retrieve a button pressed
# Think of way to make the user interface modulair. Perhaps create a modulair menu, 
#     for each menu item import a file and allow that file to write to the screen,
#     MultiThreading/multiprocessing for tasks.
# Use classess instead of global variables, they are dirty and only need to be used 
#     for "real" GLOBAL variables, like a program state

import curses
import time
import subprocess
import sys

import terminal

from multiprocessing import Process

version = "0.1(beta)"
author = ["Timo Dekker","Dion Bosschieter"]

def sayName():
    global name
    name = input("What is your name: ")
    #subprocess.call(["/usr/bin/say", "Welcome " + name])

def drawWindow():
    global stdscr
    global win
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
    global win
    global name
    win.addstr(2,1,name)

def keyboardInterrupt():
    time.sleep(1)
    while(True):
        c = terminal.getch()
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