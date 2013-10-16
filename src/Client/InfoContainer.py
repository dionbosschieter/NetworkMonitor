import terminal
import curses
import time
from curses import panel

class InfoContainer(object):

    def __init__(self, stdscreen, title, debug_console):
        self.debug_console = debug_console
        self.height = int(terminal.height/2)
        self.width = terminal.width - 2
        self.title = title

        self.window = stdscreen.subwin(self.height,self.width,1,1)
        self.window.border(0)
        self.window.addstr(0,1,title)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()
        # Add the Border
        self.second = time.time()
        self.writebuffer = []

    def display(self):
        self.panel.top()
        self.panel.show()
        #self.window.clear()

    def hide(self):
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

    def refresh(self):
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0,1,self.title)
        #draw the last 20 log items
        #foreach i from 0 till (self.height-2) 
        #draw string on i place
        #self.writebuffer[-(self.height-2):]
        
        maxlength = (self.height-3)
        lengthofbuffer = len(self.writebuffer)
        if(lengthofbuffer>maxlength):
            startindex = (lengthofbuffer-1)-maxlength
        else:
            startindex = 0
            maxlength = lengthofbuffer

        for i in range(0, maxlength):
            #self.window.addstr(i,1,str(i))
            self.window.addstr(i+1,1,self.writebuffer[i+startindex])

        self.window.refresh()
        curses.doupdate()

    def addPacket(self, packet):
        #1 refresh per second// or 2?
        if(time.time() - self.second >= 1):
            self.writebuffer.append(packet)
            self.second = time.time()
        else:
            self.writebuffer.append(packet)

