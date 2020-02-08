#link: https://www.codewars.com/kata/563b662a59afc2b5120000c6

def nb_year(p0,percent,aug,p):
    t = 0
    
    def pop_at_time(t):
        if t == 0:
            return p0
        return (pop_at_time(t-1)*(1+percent/100)+aug)
    
    while pop_at_time(t)<p:
        t+=1
        
    return t