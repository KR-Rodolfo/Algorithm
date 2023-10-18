# Quick Sort
'''
    수행시간:
        T(n) = 2*T(n/2) + C*n --> O(n log n)
'''

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

A = list(map(int, input().split()))
result = quick_sort(A)
print(result)