# link: https://www.codewars.com/kata/56a5d994ac971f1ac500003e

def longest_consec(strarr, k):

    res = "" 
    n = len(strarr)

    if n == 0 or k > n or k <= 0:
        return(res)
        
    len_strarr = [len(strarr[i]) for i in range(n)]
    idx = 0
    len_consec = 0
    
    for i in range(n-k+1):
        len_consec_tmp = sum([len_strarr[i+j] for j in range(k)])
        if len_consec_tmp > len_consec:
            idx = i
            len_consec = len_consec_tmp
            
    for i in range(k):
        res += strarr[idx+i]
        
    return(res)