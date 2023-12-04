def print_subset(x):
	print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
	v_sum = 0
	global find_subset
	for i in range(k):
		v_sum += x[i] * A[i]
		
	if k == len(A):
		if v_sum == S:
			find_subset = True
			print_subset(x)
	else:
		# code for x[k] = 1 and x[k] = 0
		if v_sum + A[k] <= S:
			x[k] = 1
			subset_sum(k + 1)
		x[k] = 0
		subset_sum(k + 1)

A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
find_subset = False
subset_sum(0)
if find_subset == False:
	print([])