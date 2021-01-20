import menu
import sub_conv_menu



def sure():

    print("Are you sure you want to quit?")
    print("1) Yes.\n2) No.")

    user_in = int(input(": "))

    if user_in == 1:
        exit()
    elif user_in == 2:
        menu.menu()
    else:
        print("Invalid option!")
        sure()


def end():

    print("1) Menu.\n2) Quit.")

    user_input = int(input(": "))

    if user_input == 1:
        menu.menu()
    elif user_input == 2:
        sure()
    else:
        print("Invalid option!")
        end()


def conv_menu():
    print("What are we converting?")

    print("1) Tempature.\n2) Main Menu.")

    user_input = int(input(": "))

    if user_input == 1:
        sub_conv_menu.temp_conv_menu()
    elif user_input == 2:
        menu.menu()
    else:
        print("Invalid option!")
        conv_menu()

