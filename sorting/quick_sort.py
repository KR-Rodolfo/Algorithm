# Quick Sort 알고리즘의 두 가지 형태
'''
    수행시간:
        평균, BestCase:
            T(n) = 2*T(n/2) + C*n --> O(n log n)
        WorstCase: 
            T(n) = T(n-1) + C*n  --> O(n^2)
'''


# stable, not-in-place
def quick_sort(A):
    if len(A) <= 1:
        return A
    
    S, M, R = [], [], [] # in-place(X)
    pivot = A[0]

    # C * n
    for x in A: # stable(O)
        if x < pivot:
            S.append(x)
        elif x > pivot:
            R.append(x)
        else:
            M.append(x)

    # 2*T(n/2) + C*n(list끼리의 합연산)
    return quick_sort(S) + M + quick_sort(R)

# in-place, unstable
def quick_sort2(A, first, last):
    if first >= last:
        return
    pivot = A[first]
    left = first + 1
    right = last

    while left <= right:
        while left <= last and A[left] < pivot:
            left += 1
        while right > first and A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    
    A[first], A[right] = A[right], A[first]
    quick_sort2(A, first, right - 1)
    quick_sort2(A, right + 1, last)

    

A = list(map(int, input().split()))
result = quick_sort(A)
print(result)

quick_sort2(A, 0, len(A) - 1)
print(A)
