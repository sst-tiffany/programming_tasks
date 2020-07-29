def table_column(table, col_n):
    return [row[col_n] for row in table]


def result_keys(left_table, right_table, join_type='INNER', left_on=0, right_on=0):
    if join_type == 'INNER':
        result_keys = set(table_column(left_table, left_on)) & set(table_column(right_table, right_on))
    elif join_type == 'LEFT':
        result_keys = set(table_column(left_table, left_on))
    elif join_type == 'RIGHT':
        result_keys = set(table_column(right_table, right_on))
    elif join_type == 'FULL':
        result_keys = set(table_column(left_table, left_on)) | set(table_column(right_table, right_on))
    return result_keys


def join(left_table, right_table, join_type='INNER', left_on=0, right_on=0):
    # returns result table for join operation on some pair of tables
    # join can be proceed on column #i (not only on the first one)
    left_table_width = len(left_table[0])
    right_table_width = len(right_table[0])

    keys = result_keys(left_table, right_table, join_type, left_on, right_on)

    left_table_res = [row for row in left_table if row[left_on] in keys]
    right_table_res = [row for row in right_table if row[right_on] in keys]

    result_table = []
    for key in keys:
        key_left_table = [row for row in left_table if row[left_on] == key]
        key_right_table = [row for row in right_table if row[right_on] == key]

        if key_left_table and key_right_table:
            for row_left in key_left_table:
                for row_right in key_right_table:
                    result_table.append(
                        [key] +
                        [row_left[i] for i in range(left_table_width) if i != left_on] +
                        [row_right[i] for i in range(right_table_width) if i != right_on]
                    )

        elif key_left_table:
            for row_left in key_left_table:
                result_table.append(
                    [key] +
                    [row_left[i] for i in range(left_table_width) if i != left_on] +
                    ['NULL' for i in range(right_table_width) if i != right_on]
                )

        elif key_right_table:
            for row_right in key_right_table:
                result_table.append(
                    [key] +
                    ['NULL' for i in range(left_table_width) if i != left_on] +
                    [row_right[i] for i in range(right_table_width) if i != right_on]
                )

    return result_table


# table T1 input
left_len = int(input())
left_table = []
for i in range(left_len):
    left_table.append([int(x) for x in input().split()])

# table T2 input
right_len = int(input())

right_table = []
for i in range(right_len):
    right_table.append([int(x) for x in input().split()])

# join_type
join_type = input()

# result calculation
result_table = join(left_table, right_table, join_type)
print(len(result_table))
for row in result_table:
    print(' '.join([str(val) for val in row]))
