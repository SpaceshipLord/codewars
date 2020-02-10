# link: https://www.codewars.com/kata/5d5a7525207a674b71aa25b5

# my first solution
def odd_row(n):

    init_odd = 2*(n*(n+1)//2-n)+1
    fin_odd = 2*((n+1)*(n+2)//2-(n+1)-1)+1
    res = [i for i in range(init_odd, fin_odd+1, 2)]

    return(res)

# the solution I would like to be able to come up with
# =============================================================================
# def odd_row(n):
#     
#     res = list(range(n*(n-1)+1, n*(n+1), 2))
#     
#     return(res)
# =============================================================================
