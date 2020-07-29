import json


def is_complex(val):
    if isinstance(val, dict) or isinstance(val, list):
        return True
    else:
        return False


def empty_value(of_type):
    empties = {
        dict: {},
        list: []
    }
    return empties[of_type]


def items(value):
    items = {
        dict: lambda x: x.items(),
        list: lambda x: enumerate(x)
    }
    return items[type(value)](value)


def add(removings, removings_inner):
    for type_value in removings:
        removings[type_value] += removings_inner[type_value]
    return removings


def removings_needed(value):
    needed = False
    removings = {
        dict: 0,
        list: 0
    }

    if is_complex(value):
        if value == empty_value(of_type=type(value)):
            needed = True
        else:
            keys_need = []
            for key, val in items(value):
                need, removings_inner = removings_needed(val)
                keys_need.append(need)
                removings = add(removings, removings_inner)
                if need:
                    removings[type(val)] += 1
            if sum(keys_need) == len(keys_need):
                needed = True

    return needed, removings


def json_clean(json_value):
    needed, removings = removings_needed(json_value)
    removings[type(json_value)] += needed

    return ' '.join([str(removings[value_type]) for value_type in [dict, list]])


# input
json_str = input()

# result calculation
json_val = json.loads(json_str)
# output
print(json_clean(json_val))
