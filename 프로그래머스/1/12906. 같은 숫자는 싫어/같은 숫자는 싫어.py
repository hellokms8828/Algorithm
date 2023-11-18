def solution(arr):
    answer = []
    answer.append(arr[0])
    del arr[0]
    for i in arr:
        a=answer.pop()
        if(a==i):
            answer.append(a)
            continue
        else:
            answer.append(a)
            answer.append(i)
            
    
    return answer