from collections import Counter

def migratoryBirds(arr):
    c = Counter(arr)
    max_count = max(c.values())
    max_nums = filter(lambda x: x[1] == max_count , c.items())
    return min(max_nums, key=lambda x: x[0])[0]
