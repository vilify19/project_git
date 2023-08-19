def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if type(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
    return flattened

nested_list = [1, 2, [3, 4, [5, [6]], 7], 8, 9, 10]
flattened_list = flatten_list(nested_list)
print(flattened_list)
