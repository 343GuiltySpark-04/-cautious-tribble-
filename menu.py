import core
import sub_menu







def menu():
    
    print("Please select a option: \n 1) Add\n 2) Subtract\n 3) Multiply\n 4) Divide\n 5) Conversion Menu\n 9) Quit")

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
        sub_menu.conv_menu()
    elif user_input_A == 9:
        sub_menu.sure()
    else:
        print("Invalid option!")
        menu()
