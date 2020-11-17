from math import floor

#Very easy board == fast
board1 = [
[0,6,0,3,0,0,8,0,4],
[5,3,7,0,9,0,0,0,0],
[0,4,0,0,0,6,3,0,7],
[0,9,0,0,5,1,2,3,8],
[0,0,0,0,0,0,0,0,0],
[7,1,3,6,2,0,0,4,0],
[3,0,6,4,0,0,0,1,0],
[0,0,0,0,6,0,5,2,3],
[1,0,2,0,0,9,0,8,0]
]

#Very hard board == slow
board2 = [
[4,0,0,0,0,0,0,0,0],
[0,0,0,0,0,9,0,0,0],
[0,0,0,0,0,0,7,8,5],
[0,0,7,0,4,8,0,5,0],
[0,0,1,3,0,0,0,0,0],
[0,0,6,0,7,0,0,0,0],
[8,6,0,0,0,0,9,0,3],
[7,0,0,0,0,5,0,6,2],
[0,0,3,7,0,0,0,0,0],
]

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




row = 0
col = 0


if(solve(board2, 0, 0)):
	print_board(board2)
else:
	print('Error: unsolvable')

