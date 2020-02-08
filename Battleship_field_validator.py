# link: 

import numpy as np

def validate_battlefield(field):
    field = np.matrix(field)
    field = np.c_[np.zeros(10),field,np.zeros(10)]
    field = np.vstack([field,np.zeros(12)])
    ships_loc = [[[-2,-2]],[[-2,-2]],[[-2,-2]],[[-2,-2]],[[-2,-2]],[[-2,-2]],[[-2,-2]],[[-2,-2]],[[-2,-2]],[[-2,-2]]]
    ships_len = [0]*10
    k = 0
    for i in range(10): 
        for j in range(1,11):
            if field[i,j] == 1:
                if (field[i,j] == 1 and field[i+1,j+1] == 1) or (field[i,j] == 1 and field[i+1,j-1] == 1): 
                    # False because of edging/bordering ships
                    return(False)
                new = True
                for l in range(10):
                    if (ships_loc[l][-1][0] == i-1 and ships_loc[l][-1][1] == j) or (ships_loc[l][-1][1] == j-1 and ships_loc[l][-1][0] == i):
                        new = False
                        ships_loc[l].append([i,j])    
                if new:
                    try:
                        ships_loc[k].append([i,j])
                        k += 1
                    except IndexError:
                        # False because of too many ships
                        return(False)
    for i in range(10):
        ships_len[i] = len(ships_loc[i])-1 
    if sorted(ships_len) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]:
        # False because of wrong composition
        return(True)
    return(False)