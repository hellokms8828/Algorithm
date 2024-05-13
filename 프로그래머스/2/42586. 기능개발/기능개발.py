from collections import deque

def solution(progresses, speeds):
    answer = []
    
    deq = deque()
    for i in (progresses):
        deq.append(i)
    
    while(True):
        cnt = 0 
        for i in range(len(speeds)):
            deq[i]+=speeds[i]
       
        for i in range(len(speeds)):
            n=deq.popleft()
            if(n<100):
                deq.appendleft(n)
                break
            else:
                del speeds[0]
                cnt+=1
            
        if(cnt>0):
            answer.append(cnt)
            
        if(sum(answer)==len(progresses)):
            break
                
    return answer