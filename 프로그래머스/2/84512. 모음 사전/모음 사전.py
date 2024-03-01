
from itertools import product
def solution(word):
    answer = 0
    myList = []
    for i in range(1,6):
        myList.extend(list(map(''.join, product(['A','E','I','O','U'], repeat=i))))
    myList.sort()
    
    return myList.index(word)+1