
from itertools import product
def solution(word):
    myList = []
    for i in range(1,6):
        myList.extend(list(map(''.join, product(['A','E','I','O','U'], repeat=i))))
    print(myList)
    myList.sort()
    
    return myList.index(word)+1