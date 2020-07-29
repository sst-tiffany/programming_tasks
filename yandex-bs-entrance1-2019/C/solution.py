def recurrent_sequence_part(indexes):
    n = max(indexes)
    set_of_indexes = set(indexes)
    sequence_part = {
        0: 0,
        1: 1,
        2: 2,
        3: 2
    }

    for i in range(4, max(4, n + 1)):
        sequence_part[i] = sequence_part[i - 1] + sequence_part[i - 3]
        if i - 4 not in set_of_indexes:
            del sequence_part[i - 4]

    return sequence_part


# input
indexes_cnt = int(input())
indexes = [int(x) for x in input().split()]

# sequence_part construction
sequence_part = recurrent_sequence_part(indexes)
# result calculation
result_values = ' '.join([str(sequence_part[i]) for i in indexes])

# output
print(result_values)
