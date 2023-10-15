# 이진탐색을 이용한 Insertion Sort
'''
    이진탐색 알고리즘을 이용해 정렬할 값이 위치할 index를 O(log n)시간에 구할 수 있다.
    하지만 최악의 경우(입력된 배열이 내림차순)일때, 값을 이동시키는 과정에서 O(n)시간이 소요된다.
        => n - 1번의 라운드를 반복함으로 최악의 경우 수행시간은 O(n^2)이다.
            => 평균 수행시간: (n log n)
'''

def insertionSort_by_binarySearch(A):
    n = len(A)
    for i in range(1, n):
        index = binary_search(A, 0, i - 1, A[i])
        j = i
        while j > index:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1

    
def binary_search(A, l, r, k):
    while l <= r:
        m = (l + r) // 2
        if A[m] == k:
            return m
        elif A[m] < k:
            l =  m + 1
        else:
            r = m - 1
    return l

A = list(map(int, input().split()))
insertionSort_by_binarySearch(A)
print(A)
