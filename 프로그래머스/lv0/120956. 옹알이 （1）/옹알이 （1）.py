def solution(babbling):
    answer = 0
    baby=["aya", "ye", "woo", "ma"]
    for bbb in babbling:
        word = ""
        cnt=0
        for bb in bbb:
            word+=bb
            if(word in baby):
                word=""
                cnt+=1
        if(len(word) ==0 and cnt > 0 ):
            answer+=1
    return answer