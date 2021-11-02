import os
from abort import abort

invalid = False
invalid_backend = False

def clear(): #CLEAR CONSOLE
    os.system("cls")

def restart():
    global invalid, hours

    clear()

    print("Restart Timer")
    print("Please input how many hours until restart:")
    if invalid == True:
        print("ERROR: INVALID INPUT DETECTED")
    str_hours = input()

    if str_hours.isnumeric() and int(str_hours) > 0:
        invalid = False
        hours = int(str_hours)
    else:
        invalid = True
        clear()
        restart()

    restart_init()

def restart_init():

    time = hours * 3600 #TIME NEEDS TO BE IN SECONDS

    os.system("shutdown /r /t " + str(time))

    clear()
    finalOptions()

def finalOptions():
    global invalid_backend

    print("Please select from the following options:" + "\n" + "1: Shutdown instead of restart" + "\n" + "2: Logoff instead of restart" + "\n" + "3: Abort restart" + "\n" + "4: Close program - COMPUTER WILL RESTART AFTER TIMER HAS FINISHED COUNTING DOWN")
    if invalid_backend == True:
        print("Input the number correlating with your selection")
    str_selection = input()

    if str_selection.isnumeric() and int(str_selection) > 0 and int(str_selection) < 5:
        invalid_backend = False
        selection = int(str_selection)
    else:
        invalid_backend = True
        finalOptions()

    if selection == 1:
        os.system("shutdown /a")
        from shutdown import shutdown
        shutdown()
    elif selection == 2:
        os.system("shutdown /a")
        from logoff import logoff
        logoff()
    elif selection == 3:
        abort()
    elif selection == 4:
        exit()
    else: #THIS SHOULD NEVER TRIGGER
        invalid_backend = True
        finalOptions()
