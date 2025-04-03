from collections import Counter
def most_frequent(lst):
    if not lst:
        return None
    counter = Counter(lst) #it counts occurences of each element 
    return max(counter, key=counter.get) #finds the elements with highest count




numbers = [1,2,3,4,3,4,4,1,2,3,4,3,2]
print(most_frequent(numbers))
