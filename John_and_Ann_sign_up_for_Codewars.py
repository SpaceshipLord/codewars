# link: https://www.codewars.com/kata/57591ef494aba64d14000526

def ann(n):
    
    a_res = [0]*n
    j_res = [0]*n
    a_res[0] = 1
    j_res[0] = 0
    
    for i in range(1,n):
        t = j_res[i-1]
        j_res[i] = i - a_res[t]
        t = a_res[i-1]
        a_res[i] = i-j_res[t]
        
    return(a_res)
    
def john(n):
    
    a_res = [0]*n
    j_res = [0]*n
    a_res[0] = 1
    j_res[0] = 0
    
    for i in range(1,n):
        t = j_res[i-1]
        j_res[i] = i - a_res[t]
        t = a_res[i-1]
        a_res[i] = i-j_res[t]
        
    return(j_res)
    
def sum_john(n):
    res = john(n)
    return(sum(res))
    
def sum_ann(n):
    res = ann(n)
    return(sum(res))