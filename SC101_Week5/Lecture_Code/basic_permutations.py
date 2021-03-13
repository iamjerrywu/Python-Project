"""
File: basic_permutations.py
Name:
-----------------------------
This program finds all the 3-digits binary permutations
by calling a recursive function binary_permutations.
Students will find a helper function useful in advanced
recursion problems.
"""


def main():
	binary_permutations(3)

def helper(n, res):
	if n == len(res):
		print(res)
	else:
		helper(n, res + '0')
		helper(n, res + '1')

def binary_permutations(n):
	i = 0
	helper(n, "")





if __name__ == '__main__':
	main()