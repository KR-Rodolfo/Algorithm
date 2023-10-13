def insertionSort_by_binarySearch(A):
    n = len(A)
    for i in range(1, n):
        k = A[i]
        j  = i - 1
        index = binary_search(A, 0, j, k)
        while j >= index:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = k

    
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