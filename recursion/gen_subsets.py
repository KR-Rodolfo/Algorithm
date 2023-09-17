# 0 ~ n-1 까지를 원소로 하는 부분집합을 출력하는 알고리즘
# backtracking
# T(n) = 2*T(n - 1) + C
# O(2^n)
def gen_subsets(k):
    if k == n: # 0 ~ n-1까지의 모든 원소를 고려한 경우
        print(S)
    else:
        S.append(k)
        gen_subsets(k + 1) # K가 들어가는 모든 부분집함
        S.pop()
        gen_subsets(k + 1) # K가 들어가지 않는 모든 부분집합

n = int(input())
S = []
gen_subsets(0)
