from soduko_solver import solve_sudoku, print_board
from puzzle import extract_digit, find_puzzle
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import imutils
import cv2

print('loading digit classifier...')
model = load_model('digit_classifier.h5')

print('processing image...')
image = cv2.imread('puzzles/sudoku_puzzle1.jpg')
image = imutils.resize(image, width=600)
(puzzleImage, warped) = find_puzzle(image)
board = np.zeros((9,9), dtype='int')

stepX = warped.shape[1]//9
stepY = warped.shape[0]//9

cellLocs = []

for y in range(0, 9):

	row = []

	for x in range(0, 9):

		startX = x * stepX
		startY = y * stepY
		endX = (x+1) * stepX
		endY = (y+1) * stepY

		row.append((startX, startY, endX, endY))

		cell = warped[startY:endY, startX:endX]
		digit = extract_digit(cell)

		if digit is not None:

			roi = cv2.resize(digit, (28, 28))
			roi = roi.astype('float') / 255.0
			roi = img_to_array(roi)
			roi = np.expand_dims(roi, axis=0)

			pred = model.predict(roi).argmax(axis=1)[0]
			board[y, x] = pred

	cellLocs.append(row)

print('\n')
print('sudoku board:')
puzzle = board.tolist()
print_board(puzzle)

try:
	print('\n')
	print('solved board: ')
	solved = solve_sudoku(puzzle)
	print_board(solved)
except:
	print('ERROR...')

