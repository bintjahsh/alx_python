def square_matrix_simple(matrix=[]):
    # initialize an empty list to store squaredLists 
    newMatrix = []
    # for every sublist in the matrix
    for i in matrix:
        # square the number and add it to new matrix
        squaredList = []
        # for every number in each sublist
        for j in i:
            squaredList.append(j**2)
        newMatrix.append(squaredList)
    return newMatrix

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# new_matrix = square_matrix_simple(matrix)
# print(new_matrix)
# print(matrix)