from collections import Counter

k = int(input())
if k:
    c = Counter()
    for line in range(k):
        arr = Counter([int(el) for el in input().split(' ')][1:])
        c.update(arr)

    for key, times in sorted(c.items()):
        print(' '.join([str(key)] * times), end=" ")
