import numpy

def is_centered(arr, n):

    # debugging
    print(arr, n)

    # empty arr and centered-0
    if len(arr) == 0 and n == 0:
        return(True)
    
    # empty arr and not centered-0
    elif len(arr) == 0 and n != 0:
        return(False)
    
    arr_len = len(arr)
    
    # odd length of arr
    if (arr_len/2)%1 == .5:
        l = int(numpy.floor(arr_len/2))
        r = l
        centre_sum = arr[l]
        
    # even length of arr    
    else:
        l = int(arr_len/2-1)
        r = int(arr_len/2)
        centre_sum = arr[l]+arr[r]
        if n == 0:
            return(True)
        
    # inner most values    
    if centre_sum == n:
        return (True)
                    
    # expanding outwards
    for i in range(1, int(numpy.ceil(arr_len/2))):
        l -= 1
        r += 1
        centre_sum += arr[l]+arr[r]
        if centre_sum == n:
            return (True)
        
    # not centered-N    
    return(False)
    

