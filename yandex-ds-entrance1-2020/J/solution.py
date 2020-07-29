len_arr = int(input())
arr_inv = [1 / float(_) for _ in input().split(' ')]

cum_sum = 0
cum_arr_inv = []
for el in arr_inv:
    cum_sum += el
    cum_arr_inv.append(cum_sum)
cum_arr_inv.append(0)

intervals_cnt = int(input())
pairs = []
for i in range(intervals_cnt):
    pairs.append(input())

cache = {}
for pair in set(pairs):
    l, r = map(int, pair.split(' '))
    cache[pair] = round((r - l + 1) / (cum_arr_inv[r] - cum_arr_inv[l - 1]), 6)

for pair in pairs:
    print(cache[pair])
