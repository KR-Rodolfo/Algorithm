# zig-zag 수열 계산하기
'''
    - 수행시간: O(n^2)
    - A[k]로 끝나는 zig-zag 수열은 A[k]가 증가된 상태로 끝난 경우와 감소된 상태로 끝난 경우, 총 2가지가 존재한다.
        - 2개의 DP table이 필요하다.
'''

def zig_zag(A):
    n = len(A)
    result = []
    low = [0] * n # A[k]가 증가된 상태로 끝난 경우
    high = [0] * n # A[k]가 감소된 상태로 끝난 경우
    low[0], high[0] = 1, 1

    # O(n^2)
    for k in range(n): # 각 원소로 끝나는 zig-zag 수열의 최대 길이
        for j in range(k):
            if A[j] < A[k]: # A[k]가 high인 상태
                high[k] = max(low[j] + 1, high[k])
            if A[k] < A[j]: # A[k]가 low인 상태
                low[k] = max(high[j] + 1, low[k])
        
        # O(n)
        for i in range(n):
            result.append(max(low[i], high[i]))
    
    return max(result)

A = list(map(int, input().split()))
print(zig_zag(A))
