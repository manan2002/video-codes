def miniMaxSum(arr):
    """
        minimum sum = sum(arr) - max(arr)
        maximum sum = sum(arr) - min(arr)
        sum(), max() and min()
    """
    minSum = sum(arr) - max(arr)
    maxSum = sum(arr) - min(arr)
    print(minSum, maxSum)
