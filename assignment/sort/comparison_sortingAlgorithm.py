import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

def quick_sort(A, first, last):
	if first >= last:
		return
	global Qs
	global Qc
	pivot = A[first]
	left = first + 1
	right = last

	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			Qc += 1
		Qc += 1
		
		while right > first and A[right] > pivot:
			right -= 1
			Qc += 1
		Qc += 1
		
		if left <= right:
			A[left], A[right] = A[right], A[left]
			Qs += 1
			left += 1
			right -= 1

	A[first], A[right] = A[right], A[first]
	Qs += 1
	quick_sort(A, first, right - 1)
	quick_sort(A, right + 1, last)

#quick_sort_2를 위한 insertion sort
def insertion_sort_for_2(A, first, last):
	global QIs
	global QIc
	for i in range(first + 1, last + 1):
		j = i - 1
		while j >= first and A[j] > A[j + 1]:
			QIc += 1
			A[j], A[j + 1] = A[j + 1], A[j]
			QIs += 1
			j -= 1

#quick_sort_3를 위한 insertion sort
def insertion_sort_for_3(A, first, last):
	global IQs
	global IQc
	for i in range(first + 1, last + 1):
		j = i - 1
		while j >= first and A[j] > A[j + 1]:
			IQc += 1
			A[j], A[j + 1] = A[j + 1], A[j]
			IQs += 1
			j -= 1

# 1번 추가 점수 알고리즘  
def quick_sort_2(A, first, last):
	if last - first < 40:
		insertion_sort_for_2(A, first, last)
		return
	global QIs
	global QIc
	pivot = A[first]
	left = first + 1
	right = last

	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			QIc += 1
		QIc += 1
		
		while right > first and A[right] > pivot:
			right -= 1
			QIc += 1
		QIc += 1
		
		if left <= right:
			A[left], A[right] = A[right], A[left]
			QIs += 1
			left += 1
			right -= 1

	A[first], A[right] = A[right], A[first]
	QIs += 1
	quick_sort_2(A, first, right - 1)
	quick_sort_2(A, right + 1, last)
	
# 2번 추가 점수 알고리즘
def quick_sort_3(A, first, last):
	if last - first < 40:
		if first == 0 and last == len(A) - 1:
			insertion_sort_for_3(A, 0, last)
		return
	
	global IQs
	global IQc
	pivot = A[first]
	left = first + 1
	right = last

	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			IQc += 1
		IQc += 1
		
		while right > first and A[right] > pivot:
			right -= 1
			IQc += 1
		IQc += 1
		
		if left <= right:
			A[left], A[right] = A[right], A[left]
			IQs += 1
			left += 1
			right -= 1

	A[first], A[right] = A[right], A[first]
	IQs += 1
	quick_sort_3(A, first, right - 1)
	quick_sort_3(A, right + 1, last)
	if first == 0 and last == len(A) - 1:
		insertion_sort_for_3(A, 0, last)
	
	
def merge_sort(A, first, last):
	if first >= last: return

	m = (first + last) // 2
	L = merge_sort(A, first, m)
	R = merge_sort(A, m + 1, last)
	merge_two_list(A, first, last)	

def merge_two_list(A, first, last):
	global Ms
	global Mc
	m = (first + last) // 2
	i = first
	j = m + 1
	B = []
	
	while i <= m and j <= last:
		if A[i] <= A[j]:
			B.append(A[i])
			i += 1
		else:
			B.append(A[j])
			j += 1
		Ms += 1
		Mc += 1
			
	for k in range(i, m + 1):
		Ms += 1
		B.append(A[k])
	for k in range(j, last + 1):
		Ms += 1
		B.append(A[k])
		
	for i in range(first, last + 1):
		A[i] = B[i - first]
		Ms += 1

# 3번 추가점수 알고리즘
def merge_sort_2(A, first, last):
	if first >= last:
		return
	
	first_pivot = first + (last - first) // 3
	second_pivot = first + (last - first) // 3 * 2
	
	merge_sort_2(A, first, first_pivot)
	merge_sort_2(A, first_pivot + 1, second_pivot)
	merge_sort_2(A, second_pivot + 1, last)
	
	merge_three_list(A, first, last) # 3개의 정렬된 리스트 병합

def merge_three_list(A, first, last):
	global M2c
	global M2s
	
	first_pivot = first + (last - first) // 3
	second_pivot = first + (last - first) // 3 * 2
	
	i = first
	j = first_pivot + 1
	temp = []
	result = []
	
	while i <= first_pivot and j <= second_pivot:
		if A[i] <= A[j]:
			temp.append(A[i])
			i += 1
		else:
			temp.append(A[j])
			j += 1
		M2c += 1
		M2s += 1
		
	for k in range(i, first_pivot + 1):
		temp.append(A[k])
		M2s += 1
	for k in range(j, second_pivot + 1):
		temp.append(A[k])
		M2s += 1
	
	i = 0
	j = second_pivot + 1
	while i <= len(temp) - 1 and j <= last:
		if temp[i] <= A[j]:
			result.append(temp[i])
			i += 1
		else:
			result.append(A[j])
			j += 1
		M2c += 1
		M2s += 1
		
	for k in range(i, len(temp)):
		result.append(temp[k])
		M2s += 1
	for k in range(j, last + 1):
		result.append(A[k])
		M2s += 1
		
	for i in range(first, last + 1):
		A[i] = result[i - first]
		M2s += 1
	

def heapify_down(A, index, n):
	global Hc
	global Hs
	while 2*index + 1 < n:
		max_index = index
		if A[max_index] < A[2*index + 1]:
			Hc += 1
			max_index = 2*index + 1
		Hc += 1
		if 2*index + 2 < n and A[max_index] < A[2*index + 2]:
			Hc += 1
			max_index = 2*index + 2
		Hc += 1
		if max_index != index:
			A[max_index], A[index] = A[index], A[max_index]
			Hs += 1
			index = max_index
		else:
			break
	
def make_heap(A):
		n = len(A)
		for index in range(n - 1, -1, -1):
			heapify_down(A, index, n)

def heap_sort(A):
		global Hs
		n = len(A)
		make_heap(A)
		for i in range(n - 1, 0, -1):
			A[0], A[i] = A[i], A[0]
			Hs += 1
			heapify_down(A, 0, i)

# 4번 추가점수 알고리즘
def tim_sort(A):
	A.sort()

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
# QIc는 quick sort_2에서 리스트의 두 수를 비교한 횟수 저장
# QIs는 quick sort_2에서 두 수를 교환(swap)한 횟수 저장
# IQc는 quick sort_3에서 리스트의 두 수를 비교한 횟수 저장
# IQs는 quick sort_3에서 두 수를 교환(swap)한 횟수 저장
# M2c, M2s는 merge sort_2에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
IQc, IQs, QIc, QIs, M2c, M2s = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:] # quick_sort_2
E = A[:] # quick_sort_3
F = A[:] # merge_sort_2
G = A[:] # tim_sort

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("")
print("Quick sort_2:")
print("time =", timeit.timeit("quick_sort_2(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(QIc, QIs))

print("")
print("Quick sort_3:")
print("time =", timeit.timeit("quick_sort_3(E, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(IQc, IQs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Merge sort_2:")
print("time =", timeit.timeit("merge_sort_2(F, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(M2c, M2s))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("Tim sort:")
print("time =", timeit.timeit("tim_sort(G)", globals=globals(), number=1))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))
assert(check_sorted(F))
assert(check_sorted(G))