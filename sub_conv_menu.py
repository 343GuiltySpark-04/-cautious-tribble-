import menu
import sub_menu
import temp_conv


def temp_conv_menu():

    print("1) C to F\n2) F to C\n3) Back")

    user_input = int(input(": "))

    if user_input == 1:
        temp_conv.c_to_f()
    elif user_input == 2:
        temp_conv.f_to_c()
    else:
        sub_menu.conv_menu()

    