import math

def getTotalX(a, b):
    """
    a, b -> two arrays given.
    - the number should be a multiple of all the numbers        in a.
    - the number should be a factor of all the numbers in       b.
    """
    LCM = a[0]
    for num in a:
        LCM = int((LCM * num) / math.gcd(LCM, num))

    GCD = b[0]
    for num in b:
        GCD = math.gcd(GCD, num)

    multiplesOfLCM = list()
    multiplyBy = 1
    
    while(LCM*multiplyBy <= g):
        multiplesOfLCM.append(LCM*multiplyBy)
        multiplyBy += 1
    
    factorsOfGCD = list()
    for num in range(1,GCD+1):
        if GCD % num == 0:
            factorsOfGCD.append(num)

    multipleSet = set(multiplesOfLCM)
    factorSet = set(factorsOfGCD)
    
    answer = len(multipleSet.intesection(factorSet))
    
    return answer
