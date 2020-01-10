def diagonalDifference(arr):
    leftDiagonalSum, rightDiagonalSum = 0, 0
    arr_len = len(arr)
    i = 0
    j = 0
    while(i < arr_len):
        leftDiagonalSum += arr[i][j]
        i += 1
        j += 1
    
    i = 0
    j = arr_len - 1
    while(i < arr_len):
        rightDiagonalSum += arr[i][j]
        i += 1
        j -= 1
    
    return abs(leftDiagonalSum - rightDiagonalSum)
