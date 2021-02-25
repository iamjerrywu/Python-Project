"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	word_d = {}
	with open(FILE, "r") as f:
		for line in f:
			word_lst = line.split()
			for word in word_lst:
				new_word = string_manipulation(word)
				if new_word in word_d:
					word_d[new_word]+=1
				else:
					word_d[new_word] = 1
	print_out_d(word_d)


def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
					value of type int is the word occurrence
	---------------------------------------------------------------
	This method prints out all the info in d
	"""
	for key in d:
		print(key, "->", d[key])

def string_manipulation(word):
	ans = ""
	for ch in word:
		if ch not in PUNCTUATION:
			ans+=ch
	ans = ans.lower()
	return ans



if __name__ == '__main__':
	main()
