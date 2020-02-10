# link: https://www.codewars.com/kata/5d5ee4c35162d9001af7d699

# my first solution
def sum_of_minimums(numbers):
    
    res = sum([min(numbers[i]) for i in range(len(numbers))])
    
    return(res)
    
# the solution I would like to be able to come up with 
# =============================================================================
# def sum_of_minimums(numbers):
#     
#     res = sum(map(min, numbers))
#     
#     return(res)
# =============================================================================
