from itertools import combinations
def solution(nums):
    answer = 0
    def isprime(numlist):
        total=sum(numlist)
        for i in range(2,total):
            if (total%i==0):
                return False
        return True
    
    comlist=list(map(list, combinations(nums,3)))
    for i in comlist:
        if (isprime(i)):
            answer+=1

    return answer