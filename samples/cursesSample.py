import curses
import time

stdscr = curses.initscr()

def show_progress():
    #Create a window object.
    win = curses.newwin(4,32,14,10)
    # Add the Border
    win.border(0)
    # Current text: Progress
    win.addstr(0,1,"Progress bar")
    win.addstr(2,1,"Progress ")
    # This is to move the progress bar per iteration.
    pos = 10
    # Random number I chose for demonstration.
    for i in range(15):
        # Add '.' for each iteration.
        win.addstr(2,pos,".")
        # Refresh or we'll never see it.
        win.refresh()
        # Here is where you can customize for data/percentage.
        time.sleep(0.05)
        # Need to move up or we'll just redraw the same cell!
        pos += 1
    # Current text: Progress ............... Done!
    win.addstr(2,26,"Done!")
    # Gotta show our changes.
    win.refresh()
    # Without this the bar fades too quickly for this example.
    time.sleep(0.5)

show_progress()
curses.endwin()