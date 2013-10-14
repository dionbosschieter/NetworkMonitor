#!/usr/bin/env python3

import curses
import terminal
import subprocess
from curses import panel
from Menu import Menu
from Window import Window
from InfoContainer import InfoContainer
from DebugConsole import DebugConsole

class NetworkMonitor(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        title = "Network Monitor - Dion Bosschieter, Timo Dekker - Version: 0.1"

        debug_console = DebugConsole(self.screen, "Debugging information")
        main_window = Window(title, self.screen)
        info_container = InfoContainer(self.screen, "Netwerk info", debug_console)

        submenu_items = [
                ('beep', curses.beep),
                ('flash', curses.flash)
                ]
        submenu = Menu(submenu_items, self.screen, "Submenu", debug_console, info_container)

        main_menu_items = [
                ('Connect...', curses.beep),
                ('Disconnect...', curses.flash),
                ('Submenu', submenu.display),
                ('Exit', exit)
                ]
        main_menu = Menu(main_menu_items, self.screen, "Main menu", debug_console, info_container)
        
        main_window.display()
        info_container.display()
        debug_console.display()
        debug_console.log("Logging initialized")
        debug_console.log("Network Monitor has started")
        
        
        
        #listen for keypressess
        while(True):
            c = terminal.getch()
            if c == 'q': break
            elif c == 'h': main_menu.display()
            elif c == 'p': info_container.addPacket("ICMP naar 8.8.8.8")
        #system quit()

if __name__ == '__main__':
    curses.wrapper(NetworkMonitor)
