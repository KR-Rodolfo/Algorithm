# Selection 문제
'''
    입력: 리스트와 k(1 <= k <= n)값이 주어진다.
    출력: K번째로 작은 수를 찾아 리턴한다.
    목표: 비교횟수를 최대한 줄인다.
'''

# quick-select 알고리즘
'''
    k번째 수를 찾는 알고리즘
    
    1. best-case:
        매번 적절한 pivot에 의하여 리스트가 n/2로 나누어 지는 경우:
            T(n) = T(n/2) + C*n --> O(n)
    2. worst-case:
        오름차순의 경우, 아래와 같이 pivot을 선정하면 pivot을 제외한 n-1개의 원소를 가진 리스트가 다시 재귀호출된다:
            T(n) = T(n-1) + C*n --> O(n^2)
    
    평균적으로 quick-select 알고리즘의 경우 평균적으로 O(n)시간만에 동작하는 알고리즘이다.
'''
def quick_select(A, k):
    pivot = A[0] # 임의의 pivot 값 설정
    S, M, L, = [], [], []

    # pivot 보다 작은 수는 S, 큰 수는 L, 같은 수는 M에 삽입한다.
    # n번 반복 --> c*n
    for x in A:
        if x < pivot:
            S.append(x)
        elif x > pivot:
            L.append(x)
        else:
            M.append(x)

    # k번째 원소가 속한 리스트만을 다시 재귀적으로 호출한다.
    if k <= len(S):
        return quick_select(S, k)
    elif k > len(S) + len(M):
        return quick_select(L, k - len(S) - len(M))
    else:
        return pivot
    
A = list(map(int, input().split()))
k = int(input())
result = quick_select(A, k)
print(result)