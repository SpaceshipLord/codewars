# link: https://www.codewars.com/kata/5709bdd2f088096786000008

def super_size(n):
    
    # get integer into n_list of strings
    n_list = [i for i in str(n)]
    
    # sort n_list
    n_list.sort(reverse = True)
    
    # string list back together as res
    res = "".join(n_list)
    
    # return res as an integer
    return(int(res))