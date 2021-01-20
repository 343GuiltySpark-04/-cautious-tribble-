import menu
import sub_conv_menu
import perc_finder



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

    print("1) Tempature.\n2) Back.")

    user_input = int(input(": "))

    if user_input == 1:
        sub_conv_menu.temp_conv_menu()
    elif user_input == 2:
        menu.menu()
    else:
        print("Invalid option!")
        conv_menu()



def credits():

    print("-----------------------------------------------------")

    print("Sparks Multipurpose Caclulator Was Created By: ")

    print("-----------------------------------------------------")

    print("Tristan Adams (AKA 343GuiltySpark-04)")

    print("-----------------------------------------------------")

    print("Enter 1 when done")

    user_input = int(input(": "))

    if user_input == 1:
        menu.menu()
    else:
        print("Invalid option!")
        credits()

    





def page_2():

    print("------------------------")

    print("!!!Page 2!!!")

    print("------------------------")

    print("Please select a option: \n 1) Conversion menu\n 2) Percentage finder\n 3) Credits\n 4) Back")

    user_input = int(input(": "))

    if user_input == 1:
        conv_menu()
    elif user_input == 2:
        perc_finder.perc_find()
    elif user_input == 3:
        credits()
    elif user_input == 4:
        menu.menu()
    else:
        print("Invalid option!")
        page_2()
