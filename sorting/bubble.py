# Bubble Sort
'''
    한번의 round 마다 큰값들이 정렬된다.

    round 마다,
        비교 횟수: n번
        이동 횟수: 최악의 경우(입력된 배열이 내림차순인 경우), n번
    round가 총 n번 반복함으로, 수행시간은 O(n^2)이다.

'''
def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(1, n):
            if A[j - 1] > A[j]:
                A[j], A[j-1] = A[j - 1], A[j]

A = list(map(int, input().split()))
bubble_sort(A)
print(A)
