import terminal
import curses
from curses import panel

class DebugConsole(object):

    def __init__(self, stdscreen, title):
        self.height = int(terminal.height/2)
        self.width = terminal.width - 2
        self.title = title

        self.window = stdscreen.subwin(self.height-1,self.width,self.height+1,1)
        self.window.border(0)
        self.window.addstr(0,1,title)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()
        # Add the Border
        self.currentLine = 1

    def display(self):
        self.panel.top()
        self.panel.show()
        #self.window.clear()

    def hide(self):
        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

    def log(self, logitem):
        self.window.border(0)
        self.window.addstr(0,1,self.title)
        if(self.currentLine < (self.height-1)):
            self.window.addstr(self.currentLine,1,logitem)
            self.window.refresh()
            curses.doupdate()
            self.currentLine += 1
