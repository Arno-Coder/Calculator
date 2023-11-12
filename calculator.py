# My calculator
def first_method(first, second) -> int:
    my_sum = first + second
    return my_sum


def second_method(first, second) -> int:
    dec = first - second
    return dec


def third_method(first, second) -> int:
    mult = first * second
    return mult


def fourth_method(first, second) -> int:
    div = first / second
    return div


def last_method(first, second) -> int:
    rem = first % second
    return rem


option_list = ["a + b", "a - b", "a * b", "a / b", "a % b", "Exit"]

user_num = 0

while True:
    print("Available options:")
    for i in option_list:
        print(f"{int(option_list.index(i)) + 1}. {i}")

    try:
        user_num = int(input("Enter option: "))
    except ValueError:
        print("You have entered a string, enter a number to continue using the calculator.")

    if int(user_num) >= 6:
        break

    if 1 <= int(user_num) < 6:

        print(f"{user_num}. {option_list[user_num - 1]}")

        try:
            a = int(input("insert a: "))
            b = int(input("insert b: "))
        except ValueError:
            print("You have entered a string, enter a number to continue using the calculator.")

        if user_num == 1:
            print(f"Answer a+b: {first_method(a, b)}")

        if user_num == 2:
            print(f"Answer a-b: {second_method(a, b)}")

        if user_num == 3:
            print(f"Answer a*b: {third_method(a, b)}")

        if user_num == 4:
            print(f"Answer a/b: {fourth_method(a, b)}")

        if user_num == 5:
            print(f"Answer a%b: {last_method(a, b)}")

    else:
        print("Invalid option. Please choose a number between 1 and 6.")