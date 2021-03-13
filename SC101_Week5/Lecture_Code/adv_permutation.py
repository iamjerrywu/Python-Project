"""
File: adv_permutation.py
Name:
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def helper(i, visited, lst, res):
	if len(res) == len(lst):
		print(res)
	else:
		for i in range(len(lst)):
			# if not visited[i]:
			if lst[i] not in res:
				# visited[i] = True

				res.append(lst[i])
				helper(i, visited, lst, res)
				res.pop()
				# visited[i] = False

def permutation(lst):
	res = []
	visited = [False] * len(lst)
	helper(0, visited, lst, res)





if __name__ == '__main__':
	main()