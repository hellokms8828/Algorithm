def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    c_len = len(citations)
    print(citations)

    for i in range(len(citations)):
        h = citations[i]
        if(i+1 > h):
            break
        answer = i + 1
    
    return answer