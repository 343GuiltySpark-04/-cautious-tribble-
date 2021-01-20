import menu
import sub_menu


def perc_find():

    print("Percentage finder.")

    user_input_1 = float(input("Enter a percentage: "))

    user_input_2 = float(input("Enter a number: "))

    temp_input_1 = 0

    if user_input_1 < 1:
        temp_input_1 = user_input_1 * 100
    else:
        temp_input_1 = user_input_1

    if user_input_1 < 0:
        print("Invalid input!")
        perc_find()
    elif user_input_2 < 0:
        print("Invalid input!")
        perc_find()

    if user_input_1 >= 1:
        user_input_1 = user_input_1 / 100

    perc = user_input_1 * user_input_2

    print(temp_input_1, "% of", user_input_2, "is", perc)

    sub_menu.end()
