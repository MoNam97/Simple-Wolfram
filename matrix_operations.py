from tabulate import tabulate
import numpy as np

current_matrix = None

def show_matrix(matrix):
    if matrix is not None:
        print(tabulate(matrix))

def get_matrices():
    matrix_list = []
    size = input("Enter the size of matrix (i.e. 3 5): ")
    while size != '':
        size = [int(x) for x in size.split()]
        if len(size) != 2:
            print("Invalid size. size must be 2 integers. operation aborted!")
            return []
        m, n = size
        matrix = []
        for i in range(m):
            try:
                matrix.append([float(x) for x in input().split()])
            except ValueError:
                print("Invalid input. operation aborted!")
                return []
        matrix_list.append(np.array(matrix))
        
    return matrix_list


def mat_add():
    pass

def mat_subtract():
    pass

def mat_multiply():
    pass

def mat_determinant():
    pass

def mat_inverse():
    pass

def show_matrix_menu():
    table = []
    headers = ['ID', 'Operation']
    table.append(["1"] + ["Add"])
    table.append([""] + [""])
    table.append(["0"] + ["BACK"])
    print("===================================")
    print("Matrix Menu:")
    print()
    show_matrix(current_matrix)
    print(tabulate(table, headers=headers))