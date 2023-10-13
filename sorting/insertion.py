#Insertion Sort
'''
    한 round 당,
        비교 횟수: n번 (최악의 경우일때 -> A[n -1]의 비교횟수)
        이동 횟수(자리 바꿈 횟수): n번 ( 최악의 경우일때 -> A[n -1]의 이동횟수)
    round를 총 (n - 1)번 반복하기 때문에 수행시간은 O(n^2)이다.
'''

def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        j = i - 1
        while j >= 0 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1

A = list(map(int, input().split()))
insertion_sort(A)
print(A)