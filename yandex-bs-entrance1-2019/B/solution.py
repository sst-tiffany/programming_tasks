from collections import defaultdict


def max_frequency_keys(array):
    # returns max
    frequencies = defaultdict(lambda: 0)
    for el in array:
        frequencies[el] += 1

    max_val = max(frequencies.values())
    max_val_keys = [key for key, val in frequencies.items() if val == max_val]

    return max_val_keys


# input
array_len = int(input())
array = [int(el) for el in input().split()]

# result calculation
chosen_key = max(max_frequency_keys(array))
# output
print(chosen_key)
