"""
File: boggle.py
Name: sheng-hao wu
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
INPUT_WORD_VALID_LENGTH = 7
MIN_VALID_WORD_LENGTH = 4

prefix_dict = {}


def main():
	read_dictionary()
	# init board from input letters
	board = input_letters()
	# init 2-D visited array to record position that has been visited
	visited = [[False] * len(board[0]) for _ in range(len(board))]
	# traverse all point inside board to be start point
	res = set()
	for i in range(len(board)):
		for j in range(len(board[0])):
			visited[i][j] = True
			dfs(board, visited, j, i, board[i][j], res)
			visited[i][j] = False
	print("There are " + str(len(res)) + " words in total")


# Depth-First Search function
def dfs(board, visited, x, y, word, res):
	# if word length >= 4, then check whether it's prefix_dict and has "True" value
	if len(word) >= MIN_VALID_WORD_LENGTH and prefix_dict.get(word, False):
		# add to res, and if already exist, don't add and print
		if word not in res:
			res.add(word)
			print("Found \""+word+"\"")
	# pruning: return if word not even in prefix_dict
	if word and not has_prefix(word):
		return
	# traverse all moving options (eight directions)
	for i in range(DIRECTION_NUM):
		# move position in 8 directions
		new_x = x + DX[i]
		new_y = y + DY[i]

		# check whether it's within boundary and be visited or not, if either is yes, than continue
		if not inside_board(board, new_x, new_y) or visited[new_y][new_x]:
			continue
		# recorded the already visited position
		visited[new_y][new_x] = True
		# keep dfs recursion
		dfs(board, visited, new_x, new_y, word + board[new_y][new_x], res)
		# remove the visited position
		visited[new_y][new_x] = False


# check whether position inside board
def inside_board(board, x, y):
	return 0 <= x < len(board[0]) and 0 <= y < len(board)


# user input letters from terminal
def input_letters():
	# init empty 2-D 4*4 list
	board = [[None] * BOARD_COLUMNS for _ in range(BOARD_ROLLS)]

	roll = 0
	invalid_input = False
	while roll < 4:
		row_letters = input(str(roll + 1) + " row of letters:")
		# case insensitive
		row_letters = row_letters.lower()
		# check input letter validness
		# check if input word length not right
		if len(row_letters) != INPUT_WORD_VALID_LENGTH:
			invalid_input = True
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
	return board


# read all the words from dictionary.txt file
# prefix_dict:
# 	to store every prefix of the word from dictionary.txt file (including itself)
#   help reducing the recursive searching time (if unfinished permutation is not in prefix_dict, then can break early)
#   when the anagram reach full length, valid terms should not only in dictionary but also with "True" value
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
				# store all prefix of word (not including it self) in prefix_dict
				prefix = word[:i + 1]
				if prefix not in prefix_dict:
					prefix_dict[prefix] = False
			# store valid word from dictionary as True
			prefix_dict[word] = True


# check if sub_s in prefix_dict
def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	return sub_s in prefix_dict


if __name__ == '__main__':
	main()
