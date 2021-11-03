import os
from functools import partial
from tkinter import *
from tkinter import ttk

def abort(c):
    os.system('shutdown /a')
    c.set('Status: Timer aborted.')

def timer(a, b, c):
    try:
        time = int(round(3600 * float(a.get()))) # Verifies input is number
        if time > -1: # Verifies input is positive
            os.system('shutdown /a') # Program always attempts to abort previous timer in case one is already set.
            os.system('shutdown ' + str(b.get()) + ' /t ' + str(time))
            c.set('Status: Timer started for ' + a.get() + ' hour(s).')
        else:
            c.set('Status: VALUE ERROR - Enter a number greater than 0.')
    except ValueError:
        c.set('Status: VALUE ERROR - Enter a number greater than 0.')
        pass

def main():
    root = Tk()
    time_str = StringVar()
    usr_sel = StringVar()
    status = StringVar()
    rdo_select = [('Logoff', '/l'), ('Restart', '/r'), ('Shut down', '/s')]

    # Default status' for 2/3 variables. No default status for time_str so entry box is empty.
    usr_sel.set('/s')
    status.set('Status: Ready')

    root.title('Shut Down Timer')
    root.geometry('+%d+%d' % ((root.winfo_screenwidth() / 2) - (root.winfo_reqwidth() / 1.25), (root.winfo_screenheight() / 2) - (root.winfo_reqheight() / 2))) # Open near the center of the screen.
    mainFrame = ttk.Frame(root)
    mainFrame.grid(column = 0, row = 0, sticky = (N, W, E, S))

    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)

    # For loop to add radio buttons on left side
    for option, val in rdo_select:
        ttk.Radiobutton(mainFrame, text = option, variable = usr_sel, value = val).grid(column = 0, ipady = 2, sticky = (N, W, S)) # Using inside padding to fix spacing issues caused by 'Abort' button.

    ttk.Label(mainFrame, text = 'Time in Hours', anchor = 'center').grid(column = 2, row = 0, sticky = (W, E))

    # Create & add an entry widget, takes in string to assign to variable time_str.
    time_entry = ttk.Entry(mainFrame, width = 7, textvariable = time_str)
    time_entry.grid(column = 2, row = 1, sticky = (N, W, E, S))

    # Using partials to delay command calls.
    # Adding buttons for starting or aborting shut down timer.
    ttk.Button(mainFrame, text = 'Abort', width = 15, command = partial(abort, status)).grid(column = 2, row = 2, sticky = (W, E))
    ttk.Button(mainFrame, text = 'Start', width = 15, command = partial(timer, time_str, usr_sel, status)).grid(column = 3, row = 0, rowspan = 3, sticky = (N, W, E, S))

    # Status bar, changes based on user input. Row determined by length of radio button list.
    ttk.Label(mainFrame, textvariable = status).grid(column = 0, row = len(rdo_select) + 1, columnspan = 4, sticky = (W))

    # For loop to add padding to every UI widget.
    for child in mainFrame.winfo_children():
        child.grid_configure(padx = 5, pady = 4)

    # Separators for organization, length determined by length of radio button list.
    ttk.Separator(mainFrame, orient = 'vertical').grid(column = 1, row = 0, rowspan = len(rdo_select), sticky = (N, S))
    ttk.Separator(mainFrame, orient = 'horizontal').grid(column = 0, row = len(rdo_select), columnspan = 4, sticky = (W, E))

    time_entry.focus() # Default focus on entry widget
    root.bind('<Return>', lambda event:timer(time_str, usr_sel, status)) # Using lambda to delay command call

    root.resizable(False, False) # Prevent window from being resized.
    root.mainloop()

if __name__ == '__main__':
    main()
