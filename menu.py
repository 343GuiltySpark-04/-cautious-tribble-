import core
import sub_menu
import perc_finder








def menu():

    print("--------------------------------------------------------")

    print("!!!Welcome to Sparks Multipurpose Calculator!!!")

    print("--------------------------------------------------------")
    
    print("Please select a option: \n 1) Add\n 2) Subtract\n 3) Multiply\n 4) Divide\n 5) Page 2\n 0) Quit")

    user_input_A = 100

    #so it won't default to quit if no input is entered

    user_input_A = int(input(": "))
    if user_input_A == 1:
        core.add()
    elif user_input_A == 2:
        core.subtract()
    elif user_input_A == 3:
        core.multi()
    elif user_input_A == 4:
        core.main.divide()
    elif user_input_A == 5:
        sub_menu.page_2()
    elif user_input_A == 0:
        sub_menu.sure()
    elif user_input_A == 1114:
        print("MEOW!")
        menu()
    else:
        print("Invalid option!")
        menu()
