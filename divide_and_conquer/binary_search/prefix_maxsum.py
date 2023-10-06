# 최대구간 합 문제

# O(n^2)에 동작하는 알고리즘
'''
    - p[i] = A[0] + A[1] + ... + A[i-1] + A[i]
    - A[i] ~ A[j] = p[j] - p[i - 1]
'''
def prefix_max_sum_1(A):
    n = len(A)
    p = [0] * n
    p[0] = A[0]

    for i in range(1, n): # 리스트 p 초기화 -> C*n
        p[i] = p[i - 1] + A[i]
    
    curr_max = 0
    for j in range(n - 1, -1, -1): # O(n^2)
        for i in range(n):
            if p[j] - p[i] > curr_max:
                curr_max = p[j] - p[i]

    return curr_max
            
# O(n log n)에 동작하는 알고리즘
'''
    - T(n) = 2*T(n/2) + C*n --> O(n log n)
    - 최대구간이 있는 위치는 왼쪽 절반, 오른쪽 절반, 왼쪽과 오른쪽은 걸친 위치에 있는 경우 총 3가지이다. 
'''
def prefix_max_sum_2(A, s, e):
    if s == e:
        return A[s]
    
    m = (s + e) // 2

    # 왼쪽 절반에서의 최대구간 합 L -> T(n/2)
    L = prefix_max_sum_2(A, s, m)

    # 오른쪽 절반에서의 최대구간 합 R -> T(n/2)
    R = prefix_max_sum_2(A, m + 1, e)

    # 오른쪽 절반과 왼쪽 절반에 걸친 최대구간 합 M -> C*n
    left_max = A[m]
    curr_sum = 0
    for i in range(m, s - 1, -1): # n/2 * C
        curr_sum += A[i]
        if curr_sum > left_max:
            left_max = curr_sum
    
    right_max = A[m + 1]
    curr_sum = 0
    for i in range(m + 1, e + 1): # n/2 * C
        curr_sum += A[i]
        if curr_sum > right_max:
            right_max = curr_sum

    M = left_max + right_max

    return max(L, R, M)


#A = list(map(int, input().split()))
A = [-2,4,7,-4,2,7,5,-3]
print(prefix_max_sum_1(A)) # 21
print(prefix_max_sum_2(A, 0, len(A) - 1)) # 21
