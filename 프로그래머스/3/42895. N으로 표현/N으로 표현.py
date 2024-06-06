def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    for i in range(1, 9):  # 1부터 8까지
        for j in range(1, i):  # 1부터 i-1까지
            for a in dp[j]:  # dp[j]의 각 원소
                for b in dp[i - j]:  # dp[i-j]의 각 원소
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        if number in dp[i]:
            return i
    
    return -1

# 예시 실행
print(solution(5, 12))  # 기댓값: 4
