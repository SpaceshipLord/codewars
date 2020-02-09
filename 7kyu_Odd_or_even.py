# link: https://www.codewars.com/kata/5949481f86420f59480000e7

def odd_or_even(arr):
    
    # sum up all elements in arr
    sum_arr = sum(arr)
    
    # return "even" if sum is even
    if sum_arr%2 == 0:
        return("even")
        
    # return "odd" if sum is off
    else:
        return("odd")