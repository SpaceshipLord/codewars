#link: https://www.codewars.com/kata/5813d19765d81c592200001a

def dont_give_me_five(start,end):
    numbers=[]
    for idx in range(start,end+1):
        numbers.append(str(idx))
    fives = [s for s in numbers if "5" in s]
    return(len(numbers)-len(fives))