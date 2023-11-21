# 주어진 문자열과 그 문자열을 reverse한 문자열간의 최장 공통 부문자열이 최장 회문 부분자열이다.
'''
	- 수행시간
		1, 문자열은 뒤집는데 소요되는 시간: O(n)
		2, LCS: O(n^2)
		=> O(n) + O(n^2) = O(n^2)
		   수행시간은 O(n^2)이다.
'''

def palindrome_sub(sequence):
	n = len(sequence)
	reverse = ''
	for i in range(n - 1, -1, -1): # O(n)
		reverse = reverse + sequence[i]
	
	DP_table = [[0] * (n + 1) for _ in range(n + 1)]
	
	for i in range(1, n + 1): # O(n^2)
		for j in range(1, n + 1):
			if sequence[i - 1] != reverse[j - 1]:
				DP_table[i][j] = max(DP_table[i - 1][j], DP_table[i][j - 1])
			else:
				DP_table[i][j] = DP_table[i - 1][j - 1] + 1
	return DP_table[n][n]

sequence = input()
print(palindrome_sub(sequence))
