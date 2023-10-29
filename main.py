from tabulate import tabulate
import re
import copy
import matplotlib.pyplot as plt
import numpy as np

state = 'MAIN'
calc_value = 0
expression = []

# [ ] TODO: Debug the UI concerning empty lines
# [ ] TODO: make the input taking format consistent


def show_main_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Calculation"])
    table.append(["3"] + ["Polynomial Computation"])

    # table.append([""] + [""])
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
        x **= 1 / number
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


def print_expr():
    print("Current Expression:\t", end='')
    for w in expression:
        print(w, end=' ')


def show_poly_menu():
    table = []
    headers = ["ID", "Command"]
    table.append(["1"] + ["Enter Expression"])
    table.append(["2"] + ["Compute at Specific Point"])
    table.append(["3"] + ["Plot"])
    table.append(["0"] + ["BACK"])
    print("===================================")
    print("Polynomial Menu:")
    print()
    print_expr()
    print()
    print(tabulate(table, headers=headers))


def show_menu():
    if state == 'MAIN':
        show_main_menu()
    elif state == 'CALCULATION':
        show_calc_menu()
    elif state == 'POLYNOMIAL':
        show_poly_menu()


def handle_input_main(x):
    global state
    if x == '0':
        exit()
    elif x == '1':
        state = 'CALCULATION'
    elif x == '3':
        state = 'POLYNOMIAL'


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


def validate_expression(x):
    x = x.split(' ')
    temp_lst = []
    for t in x:
        if x != '':
            temp_lst.append(t)

    num_regex = '([-+])?\\d+(\\.\\d+)?'
    operator_regex = '[+-/*\\^]'
    s = 0
    print(temp_lst)
    for i in range(len(temp_lst)):
        w = temp_lst[i]
        if s == 0:
            if w != 'x':
                match = re.fullmatch(num_regex, w)
                if match is None:
                    print_error("Invalid Input!")
                    return None
                temp_lst[i] = float(match.group(0))
            s = 1
        elif s == 1:
            match = re.fullmatch(operator_regex, w)
            if match is None:
                print_error("Invalid Input!")
                return None
            s = 0
        else:
            print_error('Invalid Input!')
            return None
    if s == 1:
        return temp_lst
    print_error('Invalid Input!')
    return None


def calculate_expr(x):

    temp_list = copy.deepcopy(expression)

    for i in range(len(expression)):
        w = expression[i]
        if w == 'x':
            temp_list[i] = x
    i = 1
    while i < len(temp_list):
        if temp_list[i] == '^':
            a = temp_list[i-1]
            b = temp_list[i+1]
            c = a**b
            temp_list.pop(i-1)
            temp_list.pop(i-1)
            temp_list.pop(i-1)
            temp_list.insert(i-1, c)
            i -= 1
        i += 1
    i = 0
    while i < len(temp_list):
        if temp_list[i] == '/' or temp_list[i] == '*':

            a = temp_list[i - 1]
            b = temp_list[i + 1]
            if temp_list[i] == '/':
                c = a / b
            else:
                c = a * b
            temp_list.pop(i - 1)
            temp_list.pop(i - 1)
            temp_list.pop(i - 1)
            temp_list.insert(i - 1, c)
            i -= 1
        i += 1
    i = 0
    while i < len(temp_list):
        if temp_list[i] == '+' or temp_list[i] == '-':
            a = temp_list[i-1]
            b = temp_list[i+1]
            if temp_list[i] == '+':
                c = a+b
            else:
                c = a-b
            temp_list.pop(i - 1)
            temp_list.pop(i - 1)
            temp_list.pop(i - 1)
            temp_list.insert(i - 1, c)
            i -= 1
        i += 1
    return temp_list[0]


def plot(x1, x2):
    y = []
    for t in np.arange(x1, x2, 0.1):
        y.append(calculate_expr(t))
    plt.plot(np.arange(x1, x2, 0.1).tolist(), y)
    plt.show()


def handle_input_poly(x):
    global calc_value, state, expression
    if x == '0':
        state = 'MAIN'
    if x == '1':
        temp_exp = input()
        temp_exp = validate_expression(temp_exp)
        if temp_exp is not None:
            expression = temp_exp
    if x == '2':
        num = float(input())
        print("Value:", calculate_expr(num))
    if x == '3':
        num_1 = float(input())
        num_2 = float(input())
        plot(num_1, num_2)


def handle_input(x):
    if state == 'MAIN':
        handle_input_main(x)
    elif state == 'CALCULATION':
        handle_input_calc(x)
    elif state == 'POLYNOMIAL':
        handle_input_poly(x)


while True:
    show_menu()
    input_x = input()
    handle_input(input_x)
