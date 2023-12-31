# Workaholic, man!
'''
    - 할일이 5가지가 있고, 각 일에 대해선 필요한 시간이 있다. A = [2, 1, 4, 6, 3]
    - 그런데, 나에게 주어진 시간 T = 9 시간 뿐이다. T시간 이내에 최대한 많은 일을 하고 싶다.
      T시간 내에 할 수 있는 일의 최대 개수를 구하여라.
'''

# 가장 적은 시간이 드는 일들을 먼저 해야한다.
A = [2, 1, 4, 6, 3]
T = 9
cnt = 0

A.sort()
for i in range(len(A)):
    T =  T - A[i]
    if T >= 0:
        cnt += 1
    else: # T가 0보다 작은 경우는 시간이 없어 더 이상 일을 하지 못하는 경우이다.
        break

print(cnt)