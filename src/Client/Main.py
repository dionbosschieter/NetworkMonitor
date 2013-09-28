#!/usr/bin/env python2                                                       

import curses
import terminal
import subprocess                                    
from curses import panel                                                     

class Menu(object):                                                          

    def __init__(self, items, stdscreen, title):

        #center the main_menu
        height = 10
        width = 20
        x = (terminal.width/2) - (width/2)
        y = (terminal.height/2) - (height/2)
        self.title = title

        self.window = stdscreen.subwin(height,width,y,x)
        self.window.keypad(1)                            
        self.panel = panel.new_panel(self.window)
        self.panel.hide()                                                    
        panel.update_panels()

        self.position = 0                                                    
        self.items = items                                                   
        self.items.append(('exit','exit'))

    def navigate(self, n):                                                   
        self.position += n                                                   
        if self.position < 0:                                                
            self.position = 0                                                
        elif self.position >= len(self.items):                               
            self.position = len(self.items)-1                                

    def display(self):                                                       
        self.panel.top()                                                     
        self.panel.show()                                                    
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0,1,self.title)

        while True:                                                          
            self.window.refresh()                                            
            curses.doupdate()                                                
            for index, item in enumerate(self.items):                        
                if index == self.position:                                   
                    mode = curses.A_REVERSE                                  
                else:                                                        
                    mode = curses.A_NORMAL                                   

                msg = '%d. %s' % (index, item[0])                            
                self.window.addstr(1+index, 1, msg, mode)
                
        
            key = self.window.getch()                                        

            if key in [curses.KEY_ENTER, ord('\n')]:                         
                if self.position == len(self.items)-1:
                    break                                                    
                else:                                                        
                    self.items[self.position][1]()                           

            elif key == curses.KEY_UP:                                       
                self.navigate(-1)                                            

            elif key == curses.KEY_DOWN:                                     
                self.navigate(1)                                             

        self.window.clear()
        self.panel.hide()                                                    
        panel.update_panels()                                                
        curses.doupdate()

class Window(object):

    def __init__(self, title, stdscreen):
        self.window = stdscreen.subwin(0,0,0,0)
        # Add the Border
        self.window.border(0)
        self.window.addstr(0,1,title)

    def display(self):
        self.window.refresh()

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
                ('beep', curses.beep),
                ('flash', curses.flash),
                ('submenu', submenu.display)
                ]
        main_menu = Menu(main_menu_items, self.screen, "Main menu")
        main_window.display()
        
        #listen for keypressess
        while(True):
            c = terminal.getch()
            if c == 'q': break
            elif c == 'o': main_menu.display()
        #system quit()

if __name__ == '__main__':
    curses.wrapper(NetworkMonitor)
