def solution(triangle):
    
    a=[[ 0 for j in i] for i in triangle]
    
    for idx1 in range(len(triangle)-1):
        for idx2 in range(len(triangle[idx1])):
            if idx1 == 0:
                a[idx1][idx2] = triangle[idx1][idx2]
            if a[idx1+1][idx2] < a[idx1][idx2] + triangle[idx1+1][idx2]:
                a[idx1+1][idx2] = a[idx1][idx2] + triangle[idx1+1][idx2]
            if a[idx1+1][idx2+1] < a[idx1][idx2] + triangle[idx1+1][idx2+1]:
                a[idx1+1][idx2+1] = a[idx1][idx2] + triangle[idx1+1][idx2+1]
        
    
    return max(a[-1])