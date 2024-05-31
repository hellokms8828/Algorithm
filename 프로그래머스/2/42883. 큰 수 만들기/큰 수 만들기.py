def solution(number, k):
    answer = ''
    stack = list()
    
    for i in range(0,len(number)):
        a = int(number[i])
        
        while(len(stack) > 0 and a > stack[-1] and k > 0 ):
            stack.pop()
            k-= 1
        
        stack.append(a)
    
    if (k > 0):
        stack = stack[:-(k)]
    
    return ''.join(map(str,stack))