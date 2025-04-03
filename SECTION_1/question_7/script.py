def swap_dict(d):
    return {value: key for key, value in d.items()}


print(swap_dict({"a":1, "b":2}))