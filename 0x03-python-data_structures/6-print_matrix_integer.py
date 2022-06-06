#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(matrix[0])):
            if i != len(matrix[0]) - 1:
                print('{:d}'.format(row[i]), end=' ')
            else:
                print('{:d}'.format(row[i]))

if __name__ == '__main__':
    print_matrix_integer([[1, 2], [2, 4]])
