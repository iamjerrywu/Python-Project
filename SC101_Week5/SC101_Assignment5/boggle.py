"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variables
#   \|/
# --   --
#   /|\
# the eight direction that could go on board
DX = [0,  1,  1,  1,  0, -1, -1, -1]
DY = [1,  1,  0, -1, -1, -1,  0,  1]
DIRECTION_NUM = 8
BOARD_ROLLS = 4
BOARD_COLUMNS = 4
MIN_VALID_WORD_LENGTH = 4

prefix_dict = {}
word_dict = {}
cnt = [0] * 1


def main():
	read_dictionary()
	# init empty 2-D 4*4 list
	board = [[None] * BOARD_COLUMNS for _ in range(BOARD_ROLLS)]
	input_letters(board)
	print(board)

	visited = [[False] * len(board[0]) for _ in range(len(board))]
	# traverse all point inside board to be start point
	res = set()
	for i in range(len(board)):
		for j in range(len(board[0])):
			visited[i][j] = True
			dfs(board, visited, j, i, board[i][j], res)
			visited[i][j] = False
	print("There are " + str(len(res)) + " words in total")
	print(cnt[0])


def dfs(board, visited, x, y, word, res):
	cnt[0]+=1
	if len(word) >= MIN_VALID_WORD_LENGTH and word in word_dict:
		res.add(word)
		print("Found \""+word+"\"")
	if word and not has_prefix(word):
		return
	for i in range(DIRECTION_NUM):
		new_x = x + DX[i]
		new_y = y + DY[i]

		if not inside_board(board, new_x, new_y) or visited[new_y][new_x]:
			continue
		visited[new_y][new_x] = True
		dfs(board, visited, new_x, new_y, word + board[new_y][new_x], res)
		visited[new_y][new_x] = False


def inside_board(board, x, y):
	return 0 <= x < len(board[0]) and 0 <= y < len(board)


def input_letters(board):
	roll = 0
	invalid_input = False
	while roll < 4:
		row_letters = input(str(roll + 1) + " row of letters:")
		# check input letter validness
		for i in range(len(row_letters)):
			# for even space should be letters
			if i % 2 == 0 and not row_letters[i].isalpha():
				invalid_input = True
				break
			# for odd space should be ' '
			if i % 2 != 0 and row_letters[i] != ' ':
				invalid_input = True
				break
		if invalid_input:
			print("Illegal input")
		else:
			# remove ' '
			row_letters = row_letters.replace(' ', '')
			# import letters to board array
			for i in range(len(row_letters)):
				board[roll][i] = row_letters[i]
			roll += 1
		# roll back invalid input to false
		invalid_input = False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		# remove the line breaker '\n'
		words = f.read().splitlines()
		for word in words:
			for i in range(len(word) - 1):
				# store all prefix of word in prefix_dict
				prefix = word[:i + 1]
				if prefix not in prefix_dict:
					prefix_dict[prefix] = True
			# store all word in word_dict
			word_dict[word] = True


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	return sub_s in prefix_dict


if __name__ == '__main__':
	main()
