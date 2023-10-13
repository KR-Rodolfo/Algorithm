# Selection Sort
'''
    한 round 마다,
        비교 횟수: n번(get_max_index의 파라미터가 A, n-1 일때 최악의 경우의 비교 횟수이다.)
        이동 횟수: 1번
    총, n - 1번의 round를 실행함으로, 수행시간은 O(n^2)이 된다.
'''

def selection_sort(A):
    n = len(A)
    for i in range(n - 1, -1, -1):
        max_index = get_max_index(A, i) # i가 n-1일때가 최악의 입력!
        A[i], A[max_index] = A[max_index], A[i]

def get_max_index(A, index): # O(index)
    curr_max = A[0]
    max_index = 0
    for i in range(1, index + 1):
        if curr_max < A[i]:
            curr_max, max_index = A[i], i
    return max_index

A = list(map(int, input().split()))
selection_sort(A)
print(A)