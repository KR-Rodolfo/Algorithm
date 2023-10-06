# 이진 탐색: 리스트A에서 k값 찾기
# 리스트 A는 반드시 오름차순이여야 한다.

'''
    - 재귀함수를 이용한 이진탐색 알고리즘
    - T(n) = T(n/2) + C (C는 상수) --> O(log n)
'''
def binary_search_recursive(A, s, e, k):
    if s > e: # k가 리스트에 존재하지 않는 경우
        return -1
    m = (s + e) // 2
    if k < A[m]:
        return binary_search_recursive(A, s, m - 1, k)
    elif k > A[m]:
        return binary_search_recursive(A, m + 1, e, k)
    else:
        return m

'''
    - 반복문을 이용한 이진탐색 알고리즘
    - 반복문을 log n 번 반복하기 때문에 수행시간은 O(log n)이다.
    - 재귀적인 방법을 이용하지 않아 위의 알고리즘보다 공간복잡도가 더 낮다. 
'''
def binary_search_loop(A, s, e, k):
    while s <= e:
        m = (s + e) // 2
        if k < A[m]:
            e = m - 1
        elif k > A[m]:
            s = m + 1
        else:
            return m
    return -1
    
A = list(map(int, input().split()))
s, e = 0, len(A) - 1
k = int(input())

print(binary_search_recursive(A, s, e, k))
print(binary_search_loop(A, s, e, k))