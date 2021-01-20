import menu
import sub_menu




def add():

    print("Add.")

    user_input_add_1 = float(input("Enter the first number: "))

    user_input_add_2 = float(input("Enter the second number: "))

    sum_add = user_input_add_1 + user_input_add_2

    if sum_add < 0:
        sum_add = 0

    print("The sum is:", sum_add)
    sub_menu.end()

def subtract():

    print("Subtract.")

    user_input_sub_1 = float(input("Enter the first number: "))

    user_input_sub_2 = float(input("Enter the second number: "))

    sum_sub = user_input_sub_1 - user_input_sub_2

    if sum_sub < 0:
        sum_sub = 0
    

    print("The sum is:", sum_sub)
    sub_menu.end()


def multi():

    print("Multiply.")

    user_input_multi_1 = float(input("Enter the first number: "))

    user_input_multi_2 = float(input("Enter the second number: "))
    
    sum_multi = user_input_multi_1 * user_input_multi_2

    if sum_multi < 0:
        sum_multi = 0
    
    print("The sum is:", sum_multi)
    sub_menu.end()


def divide():

    print("Divide.")

    user_input_div_1 = float(input("Enter the first number: "))

    user_input_div_2 = float(input("Enter the second number: "))

    sum_div = user_input_div_1 / user_input_div_2

    if sum_div < 0:
        sum_div = 0

    print("The sum is:", sum_div)
    sub_menu.end()


