"""numberList = [[1, 2, 3, 4], [0, [1, 2, [4, 5, [10, 11]], 4], 5], 12]
print(numberList[1][1][2][2][0])"""
A = [[[],[]],[[],[]]]
matrix = [[1, 2], [3, 4]]
matrix1 = [[5, 6], [7, 8]]
for i in range(2):
    for j in range(2):
        A[i][j] = matrix[i][j]+matrix1[i][j]
print(A)



