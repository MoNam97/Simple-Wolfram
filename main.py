from tabulate import tabulate

state = 'MAIN'
calculation_value = 0

def show_main_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Calculation"])
    table.append(["0"] + ["Exit"])
    print()
    print(tabulate(table, headers=headers))


def add_func(x: int, y: list):
    for number in y:
        x += number
    return x

def add_handler():
    print("Enter the list of numbers separated by ',' to be added to the current value:")
    list_of_numbers = input()
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
    print()
    global calculation_value
    calculation_value = add_func(calculation_value, list_of_numbers)

def show_calc_menu():
    global calculation_value
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Add"])
    # table.append("              ")
    table.append(["0"] + ["BACK"])
    print("===============================")
    print("\tCALCULATION MENU")
    print()
    print("Current Value:", calculation_value)
    print()
    print(tabulate(table, headers=headers))


def show_menu():
    if state == 'MAIN':
        show_main_menu()
    if state == 'CALCULATION':
        show_calc_menu()


def handle_input_main(x):
    if x == '0':
        exit()
    if x == '1':
        global state
        state = 'CALCULATION'


def handle_input_calc(x):
    if x == '0':
        global state
        state = 'MAIN'
    elif x == '1':
        add_handler()
        


def handle_input(x):
    if state == 'MAIN':
        handle_input_main(x)
    elif state == 'CALCULATION':
        handle_input_calc(x)


while True:
    show_menu()
    input_x = input()
    handle_input(input_x)
