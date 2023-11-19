# Longest Icreasing Subsequence
'''
    - 수행시간: O(n^2)
    - zig-zag 수열 최대길이 구하기 문제와 유사
'''

def LIS(A):
    n = len(A)
    LIS = [0] * n
    LIS[0] = 1 # DP table

    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                LIS[i] = max(LIS[i], LIS[j] + 1) # 점화식
    return max(LIS)

A = list(map(int, input().split()))
print(LIS(A))
