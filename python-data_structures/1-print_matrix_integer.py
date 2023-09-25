def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        rowMatrix = ""
        for j in i:
            rowMatrix += ('{} '. format(j))
        print(rowMatrix)
        #rowMatrix = ""
    # for i in matrix:
    #     for j in matrix:
    #         newMatrix = str(matrix[[i]][:])
    #     print('{}'.format(newMatrix))

matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 6, 8]
]

print_matrix_integer(matrix)
print("--")