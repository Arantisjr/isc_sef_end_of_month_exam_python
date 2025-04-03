def multiplier(factor):
    
    def multiply_numbers(number):
        return number * factor
    return multiply_numbers

double = multiplier(2)
print(double(5))
        
