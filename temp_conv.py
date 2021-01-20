import menu
import sub_conv_menu
import sub_menu


def c_to_f():
    print("C to F")

    user_input_1 = float(input("Enter first number: "))

    sum_1 = user_input_1 * 1.5 + 32

    print(user_input_1, "C is", sum_1, "F.")

    sub_menu.end()



def f_to_c():
    print("F to C")

    user_input_1 = float(input("Enter first number: "))

    sum_1 = user_input_1 - 32 * 0.5556

    print(user_input_1, "F is", sum_1, "C.")

    sub_menu.end()
