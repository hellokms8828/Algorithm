from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting=deque(truck_weights)
    bridge_truck=deque([0]*bridge_length)
    result = deque()
    truck_num= len(truck_weights)
    total = 0 # 현재 다리에 있는 차 무게
    
    while(True):
        answer+=1
        a=0
        if waiting:
            a=waiting.popleft()
        
        b=bridge_truck.popleft() # -> [0.0.0.0.0.0.]
        
        if(b>0):
            result.append(b)
            total-=b # 현재 다리에 있는 차 무게
            if(len(result)==truck_num): # result큐가 다 차면 break
                break
        
        if(total+a > weight):#크면 total + a 
            waiting.appendleft(a)#대기큐 원상복구
            bridge_truck.append(0)
        else:#딱 맞으믄
            bridge_truck.append(a)
            total+=a
                                
            
    return answer