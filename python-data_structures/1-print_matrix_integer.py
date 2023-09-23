def print_matrix_integer(matrix=[[]]):
    # print(matrix[0][0])
    # print(matrix[1])
    # print(matrix[2])
    # for i in matrix:
    #     print('hey')
    #     for j in matrix:
    #         print("no")
        # newMatrix = str(matrix[[i]])
        # print('{}'.format(newMatrix))
        # for j in matrix:
        #     print(j)
        #     for k in matrix:
        #         print(k)
                # newMatrix = '{:d} {:d} {:d}'.format(i, j, k)
    # print(newMatrix)
    print('\n'.join([''.join(['{} '.format(item) for item in row]) 
      for row in matrix]))

# matrix = [
#     [],
#     [],
#     []
# ]

# print_matrix_integer(matrix)
# print("--")