import os
from tkinter import *
from tkinter import ttk

def abort():
    try:
        os.system('shutdown /a')
    except ValueError:
        pass

def timer(a, b):
    try:
        time = round(int(3600 * float(a.get())))
        os.system('shutdown ' + str(b.get()) + ' /t ' + str(time))
        #print('Timer command complete.') #debug
    except ValueError:
        #print('Timer command error.') #debug
        #print(a.get()) #debug
        #print(b.get()) #debug
        pass

def main():
    root = Tk()
    time_str = StringVar()
    usr_selection = StringVar()
    rdo_select = [('Logoff', '/l'), ('Restart', '/r'), ('Shutdown', '/s')]

    #TODO: Add icon
    root.title('Shutdown Timer')
    mainframe = ttk.Frame(root, padding = '5 5 5 5')
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)

    #TODO: Fix spacing between Radiobuttons.
    for option, val in rdo_select:
        ttk.Radiobutton(mainframe, text = option, variable = usr_selection, value = val).grid(column = 0, sticky = (W))

    '''
    logoff = ttk.Radiobutton(mainframe, text = 'Logoff', variable = usr_selection, value = '/l')
    logoff.grid(column = 0, row = 0, sticky = (W))
    restart = ttk.Radiobutton(mainframe, text = 'Restart', variable = usr_selection, value = '/r')
    restart.grid(column = 0, row = 1, sticky = (W))
    shutdown = ttk.Radiobutton(mainframe, text = 'Shutdown', variable = usr_selection, value = '/s')
    shutdown.grid(column = 0, row = 2, sticky = (W))
    '''

    usr_selection.set('/s')

    ttk.Label(mainframe, text = 'Time in Hours', anchor = 'center').grid(column = 1, row = 0, sticky = (W, E))

    #TODO: Check to make sure user input is number.
    time_entry = ttk.Entry(mainframe, width = 7, textvariable = time_str)
    time_entry.grid(column = 1, row = 1, sticky = (W, E))

    ttk.Button(mainframe, text = 'Abort', width = 15, command = abort).grid(column = 1, row = 2, sticky = (W, E))
    ttk.Button(mainframe, text = 'Start', width = 15, command = lambda: timer(time_str, usr_selection)).grid(column = 2, row = 0, rowspan = 3, sticky = (N, W, E, S))

    for child in mainframe.winfo_children():
        child.grid_configure(padx = 5, pady = 5)

    time_entry.focus()
    root.bind('<Return>', lambda event:timer(time_str, usr_selection))

    root.mainloop()

if __name__ == '__main__':
    main()
