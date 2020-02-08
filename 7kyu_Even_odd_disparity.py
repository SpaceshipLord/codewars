# link: https://www.codewars.com/kata/59c62f1bdcc40560a2000060

def solve(a):
    even = []
    odd = []

    for idx in range(len(a)):
        
        if type(a[idx]) == int:
            
            if a[idx] %2 == 0:
                even.append(a[idx])
                
            if a[idx] %2 != 0:
                odd.append(a[idx])
                
    return(len(even)-len(odd))