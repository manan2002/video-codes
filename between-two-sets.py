import math

def getTotalX(a, b):
    """
    We're given two arrays -> a and b.
    We need to find a number which,
     - Multiple of all numbers in a. (LCM)
     - Factor of all numbers in b. (GCD)
    """
    l = a[0]
    for num in a:
        l = int((l*num) / math.gcd(l,num))

    g = b[0]
    for num in b:
        g = math.gcd(g, num)

    multiplesOfLCM = list()
    multiplyBy = 1
    
    while(l*multiplyBy <= g):
        multiplesOfLCM.append(l*multiplyBy)
        multiplyBy += 1
    
    factorsOfGCD = list()
    for i in range(1,g+1):
        if g % i == 0:
            factorsOfGCD.append(i)

    return len(set(factorsOfGCD).intersection(set(multiplesOfLCM)))
