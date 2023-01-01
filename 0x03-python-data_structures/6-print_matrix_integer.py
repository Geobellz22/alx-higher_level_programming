#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range (len (matrix[i])):
        for j in range (len (matrix[j])):
                print("{}".format(matrix[i][j],end=''))
                if j != (len(matrix[i]) - 1):
                    print(" ", end='')

        print("")
