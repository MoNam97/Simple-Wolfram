from tabulate import tabulate

state = 'MAIN'
calc_value = 0

# [ ] TODO: Debug the UI concerning empty lines
# [ ] TODO: make the input taking format consistent

def show_main_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Calculation"])
    # table.append([""] + [""])
    table.append(["0"] + ["Exit"])
    print()
    print(tabulate(table, headers=headers))


def calc_input_parser(list_of_numbers):
    list_of_numbers = list_of_numbers.replace(" ", "")
    list_of_numbers = list_of_numbers.split(",")
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i].isdigit():
            list_of_numbers[i] = int(list_of_numbers[i])
        elif list_of_numbers[i].replace(".", "", 1).isdigit():
            list_of_numbers[i] = float(list_of_numbers[i])
        else:
            print("Invalid input")
            return
    return list_of_numbers


def add_func(x: int, y: list):
    for number in y:
        x += number
    return x

def add_handler():
    print("Enter the list of numbers separated by ',' to be added to the current value:")
    list_of_numbers = calc_input_parser(input())
    print()
    global calculation_value
    calculation_value = add_func(calculation_value, list_of_numbers)


def devide_func(x: int, y: list):
    for number in y:
        x /= number
    return round(x, 8)
# rounded because of floating point error in binary system. i.e. 12/5/3 = 0.7999999999999999

def devide_handler():
    print("Enter the list of numbers separated by ',' that current value will be divided by:")
    list_of_numbers = calc_input_parser(input())
    print()
    global calculation_value
    calculation_value = devide_func(calculation_value, list_of_numbers)


def power_func(x: int, y: list):
    for number in y:
        x **= number
    return x

def power_handler():
    print("Enter the list of numbers separated by ',' that current value will be powered by:")
    list_of_numbers = calc_input_parser(input())
    print()
    global calculation_value
    calculation_value = power_func(calculation_value, list_of_numbers)


def root_func(x: int, y: list):
    for number in y:
        x **= 1/number
    return x
    # return round(x, 8)

def root_handler():
    print("Enter the list of numbers separated by ',' that current value will be rooted by:")
    list_of_numbers = calc_input_parser(input())
    print()
    global calculation_value
    calculation_value = root_func(calculation_value, list_of_numbers)


def show_calc_menu():
    global calculation_value
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["ADD"])
    table.append(["2"] + ["SUBTRACT"])
    table.append(["3"] + ["MULTIPLY"])
    table.append(["4"] + ["DIVIDE"])
    table.append(["5"] + ["POWER"])
    table.append(["6"] + ["ROOT"])
    # table.append([""] + [""])
    # table.append(["R"] + ["RESET"])
    table.append(["0"] + ["BACK"])
    print("===================================")
    print("\tCalculation Menu")
    print()
    print("Current Value:", calc_value)
    print(tabulate(table, headers=headers))


def show_menu():
    if state == 'MAIN':
        show_main_menu()
    elif state == 'CALCULATION':
        show_calc_menu()


def handle_input_main(x):
    if x == '0':
        exit()
    elif x == '1':
        global state
        state = 'CALCULATION'


def get_numbers():
    nums = []
    next_num = input()
    while next_num != '':
        nums.append(float(next_num))
        next_num = input()
    return nums


def add(nums):
    for num in nums:
        global calc_value
        calc_value += num


def multiply(nums):
    for num in nums:
        global calc_value
        calc_value *= num


def divide(nums):
    for num in nums:
        global calc_value
        calc_value /= num


def subtract(nums):
    for num in nums:
        global calc_value
        calc_value -= num


def reset():
    global calc_value
    calc_value = 0.0


def handle_input_calc(x):
    if x == '0':
        global state
        state = 'MAIN'
    elif x == '1':
        add_handler()
    elif x == '2':
        nums = get_numbers()
        subtract(nums)
    elif x == '3':
        nums = get_numbers()
        multiply(nums)
    elif x == '4':
        devide_handler()
    elif x == '5':
        power_handler()
    elif x == '6':
        root_handler()
    elif x == 'R':
        reset()


def handle_input(x):
    if state == 'MAIN':
        handle_input_main(x)
    elif state == 'CALCULATION':
        handle_input_calc(x)


while True:
    show_menu()
    input_x = input()
    handle_input(input_x)
