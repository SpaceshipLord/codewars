# link: https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a,b,c):

    values_list  = [a, b, c]
    values_list.sort()

    return((values_list[0] + values_list[1]) > values_list[2])