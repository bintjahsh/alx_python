def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        rowMatrix = ""
        for j in i:
            rowMatrix += ('{:d}'.format(j))
            rowMatrix += ' '
            # if j != i[-1]:        
        print(rowMatrix)
        # print(len(rowMatrix))

# matrix = [
#     [1, 2, 3],
#     [2, 4, 5],
#     [3, 6, 8]
# ]

# print_matrix_integer(matrix)
# print("--")