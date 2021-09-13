import os

invalid_backend = False

def clear(): #CLEAR CONSOLE
    os.system("cls")

def abort():
    os.system("shutdown /a")

    clear()
    finalOptions()

def finalOptions():
    global invalid_backend

    print("Please select from the following options:" + "\n" + "1: Restart program" + "\n" + "2: Close program - WARNING: NO TIMER HAS BEEN SET")
    str_selection = input()

    if str_selection.isnumeric() and int(str_selection) > 0 and int(str_selection) < 3:
        invalid_backend = False
        selection = int(str_selection)
    else:
        invalid_backend = True
        finalOptions()

    if selection == 1:
        from main import main
        clear()
        main()
    elif selection == 2:
        os.system("shutdown /a") #VERIFY SHUTDOWN CANCELLED
        exit()
    else:
        clear()
        invalid_backend = True
        finalOptions()
