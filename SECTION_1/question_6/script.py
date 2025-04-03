from functools import reduce

def reduce_even_names(names):
    return reduce(lambda x, y : x + y,names)

print(reduce_even_names(["lois","Arantis","Hans"]))