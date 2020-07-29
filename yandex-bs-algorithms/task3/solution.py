first = [1, 3, 5, 7, 9]
second = [2, 4, 6, 8, 0]

rounds = 0
while rounds <= 10 ** 6:
    f, s = first[0], second[0]
    first, second = first[1:], second[1:]

    if (f > s and f != 9 and s != 0) or (f == 0 and s == 9):
        first += [f, s]
        rounds += 1
        if not len(second):
            print('first', rounds)
            break
    else:
        second += [s, f]
        rounds += 1
        if not len(first):
            print('second', rounds)
            break

else:
    print('botva')
