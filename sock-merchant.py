from collections import defaultdict, Counter

def sockMerchant(n, ar):
  """
  With defaultdict.
  """
  pairs = 0
  count = defaultdict(int)
  for item in ar:
    count[item] += 1
  
  for k, v in count.items():
    pairs += (v // 2)
  
  return pairs
  
  
def sockMerchant(n, ar):
  """
  With Counter.
  """
  pairs = 0
  count = Counter(ar)
  
  for k, v in count.items():
    pairs += (v // 2)
    
  return pairs
