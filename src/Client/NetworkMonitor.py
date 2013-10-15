#!/usr/bin/env python3

import curses
import time
import terminal
from threading import *
from curses import panel
from Menu import Menu
from Window import Window
from InfoContainer import InfoContainer
from DebugConsole import DebugConsole
from GatherInformation import GatherInformation

class NetworkMonitor(object):

    def updateScreens(self, debug_console, info_container, main_menu):
        while(True):
            if(self.threadstop == 1):
                break
            debug_console.refresh()
            info_container.refresh()
            time.sleep(1)
            #main_menu.refresh()

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        title = "Network Monitor - Dion Bosschieter, Timo Dekker - Version: 0.1"

        debug_console = DebugConsole(self.screen, "Debugging information")
        main_window = Window(title, self.screen)
        info_container = InfoContainer(self.screen, "Netwerk info", debug_console)
        gather_information = GatherInformation(info_container, debug_console, "10.3.37.50")

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
        
        self.threadstop = 0

        #create refresh deamon
        update_screens = Thread(target=self.updateScreens, args=(debug_console,info_container, main_menu))
        update_screens.daemon = True
        update_screens.start()

        #listen for keypressess
        while(True):
            c = terminal.getch()
            if c == 'q': break
            elif c == 'h':
                self.threadstop = 1
                main_menu.display()
                self.threadstop = 0
                update_screens = Thread(target=self.updateScreens, args=(debug_console,info_container, main_menu))
                update_screens.daemon = True
                update_screens.start()

            elif c == 'p': gather_information.getPackets()
            elif c == 'c': gather_information.connect()
            elif c == 'd': gather_information.disconnect()
            
        #system quit()

if __name__ == '__main__':
    curses.wrapper(NetworkMonitor)
