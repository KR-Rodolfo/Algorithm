# T(n) = T(n - 1) + C'*n + C = T(n - 1) + C*n
# O(n^2)
'''
    아래 알고리즘의 수행시간 점화식을 T(n) = T(n - 1) + C 으로 표현할 수 있을 것 같지만 그렇지 않다.
    A[1:] (슬라이싱)연산 과 list간의 합 연산은 각각 O(n)의 수행시간이 소요되기 때문이다.
'''
def reverse(A):
    if len(A) == 1:
        return A
    return reverse(A[1:]) + [A[0]]


# T(n) = T(n - 2) + C
# O(n)
def reverse_2(B, start, end):
    if start >= end:
        return
    else:
        B[start], B[end] = B[end], B[start]
        start += 1
        end -= 1
        reverse_2(B, start, end)

# T(n) = T(n - 2) + C
# O(n)
# 교제에 있는 풀이 reverse_2와 맥락은 일치한다.
def reverse_3(C, start, stop):
    if start < stop - 1:
        C[start], C[stop - 1] = C[stop - 1] ,C[start]
        reverse_3(C, start + 1, stop - 1)

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

result = reverse(A)
print(result)
reverse_2(B, 0, len(B) - 1)
print(B)
reverse_3(C, 0, len(C))
print(C)
