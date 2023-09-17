# 배열 A의 n개의 정수 중에서 최대값을 return하는 함수 3가지

# T(n) = n * C -> O(n)
def loop_array_max(A, n):
    curr_max = A[0]
    for i in range(1, n):
        if A[i] > curr_max:
            curr_max = A[i]
    return curr_max


# T(n) = T(n - 1) + C -> O(n)
def recusive_array_max_1(A, n):
    if n == 1:
        return A[0]
    return max(recusive_array_max_1(A, n - 1), A[n - 1])


# T(n) = 2*T(n/2) + C -> O(n)
def recusive_array_max_2(A, start, end):
    if start == end:
        return start
    m = (start + end) // 2
    return max(recusive_array_max_2(A, start, m), recusive_array_max_2(A, m + 1, end))

A = list(map(int, input().split()))
n = len(A)

result = loop_array_max(A, n)
print(result)
result = recusive_array_max_1(A, n)
print(result)
result = recusive_array_max_2(A, 0, n - 1)
print(result)
