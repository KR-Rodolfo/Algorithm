# 도미노 타일링
'''
    - 2 X 1 (또는 1 X 2) 도미노 여러개를 이용해 2 X n 타일을 빈틈없이 메우는 경우의 수는?
    - 입력값: n (타일의 열의 개수)
    - 출력값: 타일을 메울 수 있는 경우의 수
'''

def domino(n):
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input())
print(domino(n))