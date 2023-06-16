def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    startRow, startCol = 0,0
    endRow,endCol = len(matrix), len(matrix[0]) # know <= 1

    ret = []

    while(startRow < endRow and startCol < endCol):
        for Col in range(startCol, endCol):
            ret.append(matrix[startRow][Col])

        startRow += 1

        for Row in range(startRow, endRow):
            ret.append(matrix[Row][endCol-1])

        endCol -= 1

        if startRow < endRow:
            for Col in range(endCol-1, startCol-1, -1):
                ret.append(matrix[endRow-1][Col])

        endRow -= 1

        if startCol < endCol:
            for Row in range(endRow-1, startRow-1, -1):
                ret.append(matrix[Row][startCol])

            startCol += 1

    return ret




tests = [
    [[1,2,3],[4,5,6],[7,8,9]], # [1,2,3,6,9,8,7,4,5]
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]], # [1,2,3,4,8,12,11,10,9,5,6,7]
    [[1,2,3,4,4,5,6,7,8],[5,6,7,8,5,3,2,4,6],[9,10,11,12,3,5,7,4,1]],
    [[1],[6],[7]]
]
results = [
    [1,2,3,6,9,8,7,4,5],
    [1,2,3,4,8,12,11,10,9,5,6,7],
    [1,2,3,4,4,5,6,7,8,6,1,4,7,5,3,12,11,10,9,5,6,7,8,5,3,2,4],
    [1,6,7]
]

for index, test in enumerate(tests):
    attempt = spiralOrder(test)
    print("\nTest: {} \nAttempt: {} \nPassed: {}".format(test, attempt, results[index] == attempt))
print()