# link: https://www.codewars.com/kata/52b305bec65ea40fe90007a7

def grabscrab(word, possible_words):
    
    res = [i for i in possible_words if sorted(i) == sorted(word)]
    
    return(res)