xs = [1, 2, 3]
ys = [5, 10, 15]

print([(x, [x * y for y in ys]) for x in xs])
