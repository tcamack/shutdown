import os
from abort import abort

invalid = False
invalid_backend = False

def clear(): #CLEAR CONSOLE
    os.system("cls")

def shutdown():
    global invalid, hours

    clear()

    print("Shutdown Timer")
    print("Please input how many hours until shutdown:")
    if invalid == True:
        print("ERROR: INVALID INPUT DETECTED")
    str_hours = input()

    if str_hours.isnumeric() and int(str_hours) > 0:
        invalid = False
        hours = int(str_hours)
    else:
        invalid = True
        clear()
        shutdown()

    shutdown_init()

def shutdown_init():

    time = hours * 3600 #TIME NEEDS TO BE IN SECONDS

    os.system("shutdown /s /t " + str(time))

    clear()
    finalOptions()

def finalOptions():
    global invalid_backend

    print("Please select from the following options:" + "\n" + "1: Restart instead of shutdown" + "\n" + "2: Logoff instead of shutdown" + "\n" + "3: Abort shutdown" + "\n" + "4: Close program - COMPUTER WILL SHUTDOWN AFTER TIMER HAS FINISHED COUNTING DOWN")
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
        from restart import restart
        restart()
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
