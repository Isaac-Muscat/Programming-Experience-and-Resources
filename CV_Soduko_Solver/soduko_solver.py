from math import floor

def valid(board, x, y, digit):
	#target number at x, y
	num = digit

	#check horizontal
	for j in range(len(board[x])):
		if(board[x][j] == num):
			return False

	#check vertical
	for i in range(len(board)):
		if(board[i][y] == num):
			return False

	#check box
	box_x = floor(x/3)
	box_y = floor(y/3)

	for i in range(box_x*3, box_x*3 + 3):
		for j in range(box_y*3, box_y*3 + 3):
			if(board[i][j] == num):
				return False

	#Else good to go!
	return True

def solve(board, row, col):
	if(row == 9):
		return True
	if(board[row][col] != 0):
		if col == 8:
			if(solve(board, row+1, 0)):
				return True
		else:
			if(solve(board, row, col+1)):
				return True
	else:	
		for digit in range(1, 10):
			if(valid(board, row, col, digit)):
				board[row][col] = digit
				if col == 8:
					if(solve(board, row+1, 0)):
						return True
				else:
					if(solve(board, row, col+1)):
						return True
		board[row][col] = 0
		return False

def print_board(board):
	for line in board:
		print(line)

def solve_sudoku(board):
	row = 0
	col = 0
	if(solve(board, row, col)):
		return board
	else:
		print('Error: unsolvable')


