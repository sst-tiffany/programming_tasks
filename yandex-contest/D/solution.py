n = int(input())


def good_brackets(n):
    if n == 1:
        return ['()']
    else:
        brackets = []
        terms = [(i, n - i) for i in range(1, n // 2 + 1)]
        for terms_pair in terms:
            brs1 = good_brackets(terms_pair[0])
            brs2 = good_brackets(terms_pair[1])
            brackets += [i + j for j in brs2 for i in brs1]
            brackets += [j + i for j in brs2 for i in brs1]
            if terms_pair[0] == 1:
                brackets += ['(' + j + ')' for j in brs2]
        return sorted(set(brackets))


def print_good_brackets(n):
    print('\n'.join(good_brackets(n)))


if n:
    print_good_brackets(n)
