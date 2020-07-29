n = int(input())

curr_len = 0
max_len = 0
in_ones = False

for _ in range(n):
    el = int(input())
    if el == 1:
        if not in_ones:
            in_ones = True
        curr_len += 1
    else:
        if in_ones:
            max_len = max(max_len, curr_len)
            in_ones = False
            curr_len = 0
else:
    if in_ones:
        max_len = max(max_len, curr_len)

print(max_len)
