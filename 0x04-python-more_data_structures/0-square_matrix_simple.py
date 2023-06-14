#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    answer = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        answer.append(list(sub_matrix))
    return answer
