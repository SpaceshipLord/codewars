# link: https://www.codewars.com/kata/56c04261c3fcf33f2d000534

def doubles(maxk, maxn):
    res = 0.
    for i in range(1,maxk+1):
        sub_res = 0.
        for j in range(1,maxn+1):
            sub_res += (1/(j+1))**(2*i)
        res += 1/i*sub_res
    return(res)