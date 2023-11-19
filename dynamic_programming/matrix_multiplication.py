# 괄호치기 문제(행렬의 곱)
'''
    - 수행시간: O(n^3)
        - 테이블 엔트리 수 X 엔트리 계산 시간
        = (1/2 X n^2) X C
'''

def matrix_mul(n, p):
    # 2차원 DP table
    DP = [[10e9] * n for _ in range(n)]
    for i in range(n):
        DP[i][i] = 0

    for d in range(1, n): # d번째 대각선 채우기
        for i in range(n - d): # 행
            j = i + d # 열
            for k in range(i, j):
                DP[i][j] = min(DP[i][j], DP[i][k] + DP[k + 1][j] + p[i]*p[k + 1]*p[j + 1])
    print(DP)
    return DP[0][n-1]
    

n = int(input()) # 행렬의 개수
p = list(map(int, input().split())) # k번째 행렬은 p[k] X p[k + 1] 행렬이다.
print(matrix_mul(n, p))
