#!/usr/bin/env python3

import curses
import terminal
import subprocess
from curses import panel
from Menu import Menu
from Window import Window

class NetworkMonitor(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        title = "Network Monitor - Dion Bosschieter, Timo Dekker - Version: 0.1"

        main_window = Window(title, self.screen)

        submenu_items = [
                ('beep', curses.beep),
                ('flash', curses.flash)
                ]
        submenu = Menu(submenu_items, self.screen, "Submenu")

        main_menu_items = [
                ('Connect...', curses.beep),
                ('Disconnect...', curses.flash),
                ('Submenu', submenu.display),
                ('Exit', exit)
                ]
        main_menu = Menu(main_menu_items, self.screen, "Main menu")
        main_window.display()
        
        #listen for keypressess
        while(True):
            c = terminal.getch()
            if c == 'q': break
            elif c == 'h': main_menu.display()
        #system quit()

if __name__ == '__main__':
    curses.wrapper(NetworkMonitor)
