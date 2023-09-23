# 가장 단순한 selection 문제 예시

# 가장 큰 수 찾기(k == n)
def selection_1(L):
    curr_max = L[0]
    # 총 n-1번의 비교
    # O(n)
    for i in range(1, len(L)):
        if curr_max < L[i]:
            curr_max = L[i]
    return curr_max

# 위의 알고리즘을 토너먼트식 비교로 표현
def selection_2(L, s, e):
    if s == e:
        return L[s]
    m = (s + e) // 2
    # n - 1번의 비교를 반드시 해야한다.
    # T(n) = 2*T(n/2) + C -> O(n)
    return max(selection_2(L, s, m), selection_2(L, m + 1, e))
  
li = list(map(int, input().split()))
print(selection_1(li), selection_2(li, 0, len(li) - 1))