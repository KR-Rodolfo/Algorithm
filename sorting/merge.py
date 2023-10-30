# Merge Sort
# T(n) = 2*T(n/2) + C*n
# O(n*logn)

def merge_sort(A, first, last):
    if first >= last: return
    m = (first + last) // 2
    L = merge_sort(A, first, m) # T(n/2)
    R = merge_sort(A, m + 1, last) # T(n/2)
    merge_two_list(A, first, last) # C*n


def merge_two_list(A, first, last):
    m = (first + last) // 2
    i = first
    j = m + 1
    B = [] # not-inplace

    # 최악의 경우 n-1번, 대락 C*n 만큼의 수행시간이 소요된다.
    while i <= m and j <= last:
        if A[i] <= A[j]: # stable
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1

    # 남은 원소 처리
    # 최악의 경우, 두 반복문 중 하나의 수행시간: (n/2) * c
    for k in range(i, m + 1):
        B.append(A[k])
    for k in range(j, last + 1):
        B.append(A[k])

    for i in range(first, last + 1):
        A[i] = B[i - first] # index를 맞추고 복사해야한다.

A = list(map(int, input().split()))
merge_sort(A, 0, len(A) - 1)
print(A)
