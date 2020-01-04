from math import inf

def minimumAbsoluteDifference(arr):
    # sorting     --> O(nlog(n)) 
    arr.sort()
    minDiff = inf
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < minDiff:
            minDiff = diff
    
    return minDiff
