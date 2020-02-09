# link: https://www.codewars.com/kata/574b3b1599d8f897470018f6

def get_real_floor(n):

    # below and on european ground
    if n <= 0:
        return(n)
        
    # above ground and below coursed
    elif n < 14:
        return(n-1)
    
    # above cursed
    else:
        return(n-2)

