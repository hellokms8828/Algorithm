import heapq

def solution(operations):
    answer = []
    
    for oper in operations:
        cmd, n = oper.split(" ")
        n = int(n)
        if(cmd=="I"):
            heapq.heappush(answer, n)
            
        elif(cmd=="D"):
            if n == 1 and len(answer)>0:
                answer.sort()
                answer.pop()
                
                
            elif n == -1 and len(answer)>0:
                heapq.heappop(answer)
    
    print(answer)
    if(len(answer) > 1):
        answer.sort()
        return [answer.pop(), answer[0]]
    
    else:
        return [0,0]