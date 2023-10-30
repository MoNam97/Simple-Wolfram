from tabulate import tabulate
import numpy as np

# [ ] TODO: handle error messages printing

def show_matrix(matrix):
    if matrix is not None:
        print(tabulate(matrix))

def get_matrices(is_single_input_operator=False):
    matrix_list = []
    size = input("Enter the size of matrix (i.e. 3 5): ")
    while size != '':
        mat_size = [int(x) for x in size.split()]
        if len(mat_size) != 2:
            print("Invalid size. size must be 2 integers. operation aborted!")
            return []
        m, n = mat_size
        matrix = []
        for i in range(m):
            try:
                matrix.append([float(x) for x in input().split()])
            except ValueError:
                print("Invalid input. operation aborted!")
                return []
        # print(np.array(matrix))
        matrix_list.append(np.array(matrix))
        if is_single_input_operator:
            break
        size = input("Next matrix size: ")
        
    return matrix_list


def mat_add(matrix_list):
    result = np.zeros(matrix_list[0].shape)
    for matrix in matrix_list:
        if matrix.shape != result.shape:
            print("Invalid matrix size. operation aborted!")
            return
        result += matrix
    print("Result")
    show_matrix(result)
    print()
    


def mat_subtract():
    pass

def mat_multiply(matrix_list):
    result = matrix_list.pop(0)
    for matrix in matrix_list:
        if matrix.shape[0] != result.shape[1]:
            print("Invalid matrix size. operation aborted!")
            return
        result = np.dot(result, matrix)
    print("Result")
    show_matrix(result)
    print()


def mat_determinant():
    pass

def mat_inverse():
    pass

def show_matrix_menu():
    table = []
    headers = ['ID', 'Operation']
    table.append(["1"] + ["Add"])
    # table.append(["2"] + ["Subtract"])
    table.append(["3"] + ["Multiply"])
    table.append([""] + [""])
    table.append(["0"] + ["BACK"])
    print("===================================")
    print("Matrix Menu:")
    print()
    # show_matrix(current_matrix)
    print(tabulate(table, headers=headers))