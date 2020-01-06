from collections import Counter

def birthdayCakeCandles(ar):
  #1st approach - using .count()
  max_height = max(ar)
  return ar.count(max_height)
  
  #2nd approach - using Counter
  count = Counter(ar)
  max_height = max(ar)
  return count[max_height]
