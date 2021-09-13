import os
from logoff import logoff
from shutdown import shutdown
from restart import restart

invalid = False

def clear(): #CLEAR CONSOLE
    os.system("cls")

def main():
    global invalid, selection

    clear()

    print("Please select a number from the following options:")
    print("1: Shutdown" + "\n" + "2: Restart" + "\n" + "3: Logoff")
    if invalid == True:
        print("Input the number correlating with your selection")

    str_selection = input()

    if str_selection.isnumeric() and int(str_selection) > 0 and int(str_selection) < 4:
        invalid = False
        selection = int(str_selection)
        choice()
    else:
        invalid = True
        clear()
        main()

def choice():
    global invalid

    if selection == 1:
        shutdown()
    elif selection == 2:
        restart()
    elif selection == 3:
        logoff()
    else: #THIS SHOULD NEVER TRIGGER
        invalid = True
        main()

main()
