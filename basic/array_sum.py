# 원소의 개수가 n개인 두 배열의 모든 원소 쌍의 곱을 계산하는 알고리즘
# O(n^2)
def array_sum(A, B, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += A[i] * B[j]
    return sum

n = 5
A = [1,2,3,4,5]
B = [1,1,1,1,1]

print(array_sum(A, B, n))