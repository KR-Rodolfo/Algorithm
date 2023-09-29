import time, random

# T(n) = C*n + (0 + 1 + 2 + ... + (n-1)) * C’
# O(n^2)
def evaluate_n2(A, x):
	result = 0
	n = len(A)
	for i in range(n):
		coefficient = A[i] # 현재 계산할 항의 계수
		current_x = 1 # 현재 x의 거듭제곱 값을 저장하는 변수
		
		for j in range(i): # x^k를 O(k)에 계산하는 for문
			current_x *= x
			
		result += coefficient * current_x # result에 계산한 항의 값들을 누적한다.
		
	return result

# T(n) = C * n + C’
# O(n)
def evaluate_n(A, x):
	result = 0
	n = len(A)
	current_x = 1 # 현재 x의 거듭제곱 값을 저장하는 변수
	
	for i in range(n):
		result += A[i] * current_x # result에 계산한 항의 값들을 누적한다. A[i]는 현재 계산할 항의 계수
		current_x *= x # x^(k-1) * x = x^k을 활용
		
	return result
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [random.randint(-1000, 1000) for _ in range(n)]
# 변수 x의 값 생성
x = random.randint(-1000, 1000)

# 두 함수의 수행시간 출력
s = time.perf_counter() 
evaluate_n2(A, x) # evaluate_n2 호출
e = time.perf_counter() 
print('evaluate_n2 함수의 수행시간:', e - s)

s = time.perf_counter() 
evaluate_n(A, x) # evaluate_n 호출
e = time.perf_counter() 
print('evaluate_n 함수의 수행시간:', e - s)
