def inBucket(t, low, high):
    count = 0
    for num in t:
        if low < num < high:
            count = count + 1
    return count
