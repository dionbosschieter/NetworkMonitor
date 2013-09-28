class Window(object):

    def __init__(self, title, stdscreen):
        self.window = stdscreen.subwin(0,0,0,0)
        # Add the Border
        self.window.border(0)
        self.window.addstr(0,1,title)

    def display(self):
        self.window.refresh()