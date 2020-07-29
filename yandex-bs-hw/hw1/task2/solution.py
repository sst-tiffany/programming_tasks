xs = [1, 2, 3]
ys = [5, 10, 15]

print([(x, y, x * y) for x in xs for y in ys if not(x * y % 2)])
