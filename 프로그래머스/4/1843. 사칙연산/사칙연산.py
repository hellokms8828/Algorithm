def solution(arr):
    INF = 987654321
    n = len(arr)//2 + 1 # 숫자 개수
    
    MIN_DP = [[INF for _ in range(n)] for _ in range(n)]
    MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]

    for step in range(n):# 5
        for i in range(n-step): #0~step(점점 감소), if 3
            
            j = i + step #해당 구간의 끝, j 

            if step == 0:
                MIN_DP[i][j] = int(arr[2*i])#숫자만 넣기
                MAX_DP[i][j] = int(arr[2*i])
            else:
                for k in range(i, j):
                    if arr[2 * k + 1]  == '+':
                        MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j])
                        MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] + MIN_DP[k+1][j])
                    else:
                        MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k+1][j])
                        MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k+1][j])
                        
    return MAX_DP[0][n-1]