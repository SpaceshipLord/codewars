#link: https://www.codewars.com/kata/59c5f4e9d751df43cf000035

def solve(s):
    d = []
    n = 0
    
    for idx in range(len(s)):
        
        if s[idx] in ["a","e","i","o","u"]:
            n+=1
            
        else:
            d.append(n)
            n=0
            
        d.append(n)
    
    return(max(d))