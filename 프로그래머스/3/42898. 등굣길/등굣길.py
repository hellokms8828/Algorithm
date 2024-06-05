def solution(m, n, puddles):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0][0] = 1
    
    for x, y in puddles:
        dp[x-1][y-1] = -1
    
    for i in range(m):
        for j in range(n):
            if dp[i][j] == -1:
                dp[i][j] = 0 
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1] 
    
    return dp[m-1][n-1] % 1000000007