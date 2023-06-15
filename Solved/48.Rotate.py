def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    end = n = len(matrix) 
    start = 0

    while start < len(matrix) // 2:
        for i in range(start,n-1):
            j = i+1
            matrix[start][i], matrix[i][n-1], matrix[n-1][n-j+start], matrix[n-j+start][start] \
            = matrix[n-j+start][start], matrix[start][i], matrix[i][n-1], matrix[n-1][n-j+start]
            
        start = start + 1
        n = n - 1


# tests
tests = [
[[1,2,3],
 [4,5,6]
,[7,8,9]]

,[[5,1,9,11],
  [2,4,8,10],
  [13,3,6,7],
  [15,14,12,16]]

,[[1]]

,[[1,2], 
  [3,4]]
]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(elem) for elem in row))

for test in tests:
    rotate(test)
    print_matrix(test)
    print()