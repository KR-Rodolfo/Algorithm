# 계단을 오르는 경우의 수
'''
    1. 바닥을 1층이라고 가정
    2. 한 계단 또는 두 계단씩 오를 수 있는 경우, 1층에서 n층까지 갈 수 있는 서로 다른 경우의 수는 총 몇 가지인가?
'''

def climb_stairs(n):
    if n == 0 : return 0
    DP = [0] * (n + 1)
    DP[1] = 1
    DP[2] = 1
    for i in range(3, n + 1):
        # n층까지 가는 경우의 수 = n-2층에서 2칸 올라가는 경우 + n-1층에서 1칸 올라가는 경우
        DP[i] = DP[i - 1] + DP[i - 2]
    return DP[n]

n = int(input())
print(climb_stairs(n))