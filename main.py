from tabulate import tabulate
import matrix_operations as mo

state = 'MAIN'
calc_value = 0


def show_main_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Calculation"])
    table.append(["2"] + ["Matrix Operations"])
    table.append(["0"] + ["Exit"])
    print()
    print(tabulate(table, headers=headers))

def print_error(message):
    print("ERROR:", message)

def power(x: int, y: list):
    for number in y:
        x **= number
    return x


def root(x: int, y: list):
    for number in y:
        x **= 1/number
    return x


def show_calc_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["ADD"])
    table.append(["2"] + ["SUBTRACT"])
    table.append(["3"] + ["MULTIPLY"])
    table.append(["4"] + ["DIVIDE"])
    table.append(["5"] + ["POWER"])
    table.append(["6"] + ["ROOT"])
    table.append([""] + [""])
    table.append(["R"] + ["RESET"])
    table.append(["0"] + ["BACK"])
    print("===================================")
    print("Calculation Menu:")
    print()
    print("Current Value:", calc_value)
    print(tabulate(table, headers=headers))


def show_menu():
    if state == 'MAIN':
        show_main_menu()
    elif state == 'CALCULATION':
        show_calc_menu()
    elif state == 'MATRIX':
        mo.show_matrix_menu()


def handle_input_main(x):
    global state
    if x == '0':
        exit()
    elif x == '1':
        state = 'CALCULATION'
    elif x == '2':
        state = 'MATRIX'


def get_numbers():
    nums = []
    next_num = input()
    while next_num != '':
        if not next_num.isnumeric():
            print_error("Invalid input, Operation aborted!")
            return []
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
    global calc_value
    if x == '0':
        global state
        state = 'MAIN'
    elif x == '1':
        nums = get_numbers()
        add(nums)
    elif x == '2':
        nums = get_numbers()
        subtract(nums)
    elif x == '3':
        nums = get_numbers()
        multiply(nums)
    elif x == '4':
        nums = get_numbers()
        divide(nums)
    elif x == '5':
        nums = get_numbers()
        calc_value = power(calc_value, nums)
    elif x == '6':
        nums = get_numbers()
        calc_value = root(calc_value, nums)
    elif x == 'R':
        reset()

def handle_input_matrix(x):
    if x == '0':
        global state
        state = 'MAIN'
        print("===================================")
        print("\t  Main Menu:")
    elif x == '1':
        matrix_list =  mo.get_matrices(False)
        mo.mat_add(matrix_list)
    elif x == '2':
        matrix_list =  mo.get_matrices(False)
        mo.mat_multiply(matrix_list)
    elif x == '3':
        matrix_list =  mo.get_matrices(True)
        mo.mat_determinant(matrix_list)
    elif x == '4':
        matrix_list =  mo.get_matrices(True)
        mo.mat_inverse(matrix_list)


def handle_input(x):
    if state == 'MAIN':
        handle_input_main(x)
    elif state == 'CALCULATION':
        handle_input_calc(x)
    elif state == 'MATRIX':
        handle_input_matrix(x)


while True:
    show_menu()
    input_x = input()
    handle_input(input_x)
