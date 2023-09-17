# 배열 A의 n개의 정수 중에서 최대값을 return하는 함수

# T(n) = n * C -> O(n)
def loop_array_max(A, n):
    curr_max = A[0]
    for i in range(1, n):
        if A[i] > curr_max:
            curr_max = A[i]
    return curr_max

# T(n) = T(n - 1) + C -> O(n)
def recusive_array_max(A, n):
    if n == 1:
        return A[0]
    return max(recusive_array_max(A, n - 1), A[n - 1])

A = list(map(int, input().split()))
n = len(A)
result = recusive_array_max(A, n)
print(result)

result = loop_array_max(A, n)
print(result)
