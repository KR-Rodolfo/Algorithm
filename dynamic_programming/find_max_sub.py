# 최대 구간 합 문제
'''
    - 최대 구간 합 문제는 DP 방식으로 o(n)시간에 해결할 수 있다.
    - 입력값: 리스트 A
    - 출력값: 최대 구간의 합

    - n개의 각각의 원소들로 끝나는 최대구간을 구한다. -> DP 방식으로 해결
      리스트 A의 최대구간합은 반드시 위의 최대구간 중 하나이다.
'''

def find_maximum_section(A, n):
    if n == 0:
        return 0
    DP_table = [0] * n # DP_table[i] = A[i]로 끝나는 최대구간합 
    DP_table[0] = A[0]
    for i in range(1, n):
        DP_table[i] = max(DP_table[i - 1] + A[i], A[i])
    return max(DP_table)

A = list(map(int, input().split()))
print(find_maximum_section(A, len(A)))