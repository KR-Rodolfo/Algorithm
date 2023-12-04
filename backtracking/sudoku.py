def print_sudoku(board): # 점검용
	for row in range(9):
		if row % 3 == 0 and row != 0:
			print("- - - - - - - - - - - -")
		for col in range(9):
			if col % 3 == 0 and col != 0:
				print("| ", end="")
			if col == 8:
				print(board[row][col])
			else:
				print(str(board[row][col]) + " ", end="")
				
def is_safe(A, row, col, num):
	r = row // 3
	c = col // 3 
	for i in range(3):
		for j in range(3):
			if A[r * 3 + i][c * 3 + j] == num:
				return False
			
	for r in range(9):
		if A[r][col] == num:
			return False
		
	for c in range(9):
		if A[row][c] == num:
			return False
	
	return True
	

def solve_sudoku(A):
	# A를 sudoku 규칙에 맞게 채운다
	row = None
	col = None
	for r in range(9): # 빈칸 찾기
		for c in range(9):
			if A[r][c] == 0:
				row = r
				col = c
	if row == None:
		return True
	for num in range(1, 10):
		if is_safe(A, row, col, num):
			A[row][col] = num
			if solve_sudoku(A): # sudoko를 완성한 경우 True
				return True
	A[row][col] = 0
	return False

# 기존에 주어진 코드
def check_sudoku(A):
	# check rows
	for i in range(9):
		B = A[i][:]
		B.sort()
		s = ''.join(str(x) for x in B)
		if s != '123456789':
			return False
	# check columns
	for j in range(9):
		B = []
		for i in range(9):
			B.append(A[i][j])
		B.sort()
		s = ''.join(str(x) for x in B)
		if s != '123456789':
			return False
	# check boxes
	for i in range(3):
		for j in range(3):
			B = []
			for a in range(3):
				for b in range(3):
					B.append(A[3*i+a][3*j+b])
			B.sort()
			s = ''.join(str(x) for x in B)
			if s != '123456789':
				return False
	return True 

A = [0]*9
for i in range(9):
	row = [int(x) for x in input()]
	A[i] = row

solve_sudoku(A)
print(check_sudoku(A))