n = int(input())

batch_size = 1000
if n > 0:
    el = int(input())
    max_el = el
    print(el)
    n -= 1
    for i in range(n // batch_size):
        res_elements = set()
        for j in range(batch_size):
            el = int(input())
            res_elements.add(el)
        new_max = max(res_elements)
        if max_el in res_elements:
            res_elements.remove(max_el)
        if len(res_elements):
            print('\n'.join(map(str, sorted(res_elements))))
        max_el = new_max

    else:
        res_elements = set()
        for k in range(n - (n // batch_size) * batch_size):
            el = int(input())
            res_elements.add(el)

        if max_el in res_elements:
            res_elements.remove(max_el)
        if len(res_elements):
            print('\n'.join(map(str, sorted(res_elements))))
