def filter_even_numbers(lst,x):
    filter(list(lst), x % 2 == 0)


    print(filter_even_numbers([1,2,3,4,5,6]))