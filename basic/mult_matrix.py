# 두 개의 n X n 행렬의 곱셈
# O(n^3)
def mult_matrix(A, B, n):
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

n = 5
A = [[i for i in range(1, n + 1)] for _ in range(n)]
B = [[1 for _ in range(n)] for _ in range(n)]
print(A)
print(B)
print(mult_matrix(A, B, n))