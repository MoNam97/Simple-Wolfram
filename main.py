from tabulate import tabulate

state = 'MAIN'


def show_main_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Calculation"])
    table.append(["0"] + ["Exit"])
    print()
    print(tabulate(table, headers=headers))


def show_calc_menu():
    calculation_value = 0
    table = []
    headers = ["ID", "Command"]
    table.append(["0"] + ["BACK"])
    print("===============================")
    print("\tCALCULATION MENU")
    print()
    print("Current Value: ", calculation_value)
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


def handle_input(x):
    if state == 'MAIN':
        handle_input_main(x)
    if state == 'CALCULATION':
        handle_input_calc(x)


while True:
    show_menu()
    input_x = input()
    handle_input(input_x)
