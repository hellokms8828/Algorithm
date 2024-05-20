import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(scoville[0]<K):
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        mix = a+(b*2)
        heapq.heappush(scoville, mix)
        answer+=1
        if(len(scoville)<2 and scoville[0]<K):
            return -1
        
    return answer