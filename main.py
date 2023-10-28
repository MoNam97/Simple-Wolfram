from tabulate import tabulate

state = 'MAIN'
calc_value = 0


def show_main_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Calculation"])
    table.append(["0"] + ["Exit"])
    print()
    print(tabulate(table, headers=headers))


def show_calc_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["ADD"])
    #table.append(["2"] + ["MULTIPLY"])
    #table.append(["3"] + ["DIVIDE"])

    table.append(["0"] + ["BACK"])
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


def handle_input_calc(x):
    if x == '0':
        global state
        state = 'MAIN'
    elif x == '1':
        nums = get_numbers()
        add(nums)


def handle_input(x):
    if state == 'MAIN':
        handle_input_main(x)
    elif state == 'CALCULATION':
        handle_input_calc(x)


while True:
    show_menu()
    input_x = input()
    handle_input(input_x)
