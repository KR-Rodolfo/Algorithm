import heapq

def k_th_smallest(A):
	result = 0
	n = len(A)
	for i in range(n):
		
		# A[0] ~ A[i]까지의 A의 부분집합을 나타내는 리스트를 선언해준다. -> heap으로 사용
		subset_A = []
		
		# subset_A에 A[0] ~ A[i]까지의 값을 heap에 삽입한다. -> 최악의 경우 n번 반복!
		for j in range(i+1):
			heapq.heappush(subset_A, A[j])
		
		k = i // 3 + 1
		# subset_A는 min-heap이기 때문에 k번 pop하는 것으로 k번째로 작은 수를 찾을 수 있다. -> 최악의 경우 k = n // 3 + 1
		for _ in range(k):
			k_th_number = heapq.heappop(subset_A)
		
		# A[0] ~ A[i] 범위의 k번째 값, 즉 문제에서 요구하는 M[i]값을 누적시킨다.
		result += k_th_number
		
	return result
	
	#수행 시간 분석
	'''
		외부 for문: n번 반복한다.
		첫번째 내부 for문: 최악의 경우, 대략 n번 반복한다.
		두번째 내부 for문: 최악의 경우, 대략 n//3 + 1 번 반복한다.
		=> T(n) = n * (n + (n//3 + 1)) + C (C는 상수연산)
		결국, T(n) = n에 관한 일차식 ---> O(n^2)시간에 동작한다.
	'''

A = list(map(int, input().split()))

print(k_th_smallest(A))