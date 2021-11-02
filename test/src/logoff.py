import os
from abort import abort

invalid = False
invalid_backend = False

def clear(): #CLEAR CONSOLE
    os.system("cls")

def logoff():
    global invalid, hours

    clear()

    print("Logoff Timer")
    print("Please input how many hours until logoff:")
    if invalid == True:
        print("ERROR: INVALID INPUT DETECTED")
    str_hours = input()

    if str_hours.isnumeric() and int(str_hours) > 0:
        invalid = False
        hours = int(str_hours)
    else:
        invalid = True
        clear()
        logoff()

    logoff_init()

def logoff_init():

    time = hours * 3600 #TIME NEEDS TO BE IN SECONDS

    os.system("shutdown /l /t " + str(time))

    clear()
    finalOptions()

def finalOptions():
    global invalid_backend

    print("Please select from the following options:" + "\n" + "1: Shutdown instead of logoff" + "\n" + "2: Restart instead of logoff" + "\n" + "3: Abort logoff" + "\n" + "4: Close program - COMPUTER WILL LOGOFF AFTER TIMER HAS FINISHED COUNTING DOWN")
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
        from restart import restart
        restart()
    elif selection == 3:
        abort()
    elif selection == 4:
        exit()
    else: #THIS SHOULD NEVER TRIGGER
        invalid_backend = True
        finalOptions()
