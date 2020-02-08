#link: https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x):
    y=[]
    for idx in range(len(x)):
        if len(x[idx])==4:
            y.append(x[idx])
    return y