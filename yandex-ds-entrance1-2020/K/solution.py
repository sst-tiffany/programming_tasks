from collections import OrderedDict


n = int(input())
arr = [int(_) for _ in input().split(' ')]
od = OrderedDict.fromkeys(arr)
print(len(od))
print(' '.join(map(str, od.keys())))
