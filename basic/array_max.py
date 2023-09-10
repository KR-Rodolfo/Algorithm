# 배열 A의 n개의 정수 중에서 최대값을 return하는 함수
# O(n)
def array_max(A, n):
    curr_max = A[0]
    for i in range(1, n):
        if A[i] > curr_max:
            curr_max = A[i]
    return curr_max

A = [1,5,2,4,10,-10]
print(array_max(A, len(A)))