#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in (len(matrix)):
        for j in (len(matrix)):
            print("{}".format(matrix[i][j]), end='')
            if j < len(matrix[i]) - 1:
                print("{}".format(" "), end='')
            print()
