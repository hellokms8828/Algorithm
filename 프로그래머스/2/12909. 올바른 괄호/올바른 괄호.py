def solution(s):
    answer = True
    stack=list()
    
    for i in s:
        if(i=='('):
            stack.append(i)
        elif(i==')'):
            if(len(stack)==0):
                answer = False
                break
            stack.pop()
    
    if(len(stack)!=0):
        answer = False
    return answer