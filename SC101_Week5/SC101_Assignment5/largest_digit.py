"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def helper(n, ans):
	# base condition for recursion, if no more digits in n
	if n == 0:
		return ans
	# to calculate digit in n, simply //10 can get in from LSB to MSB order
	return helper(n//10, max(n%10, ans))


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	ans = 0
	# call helper to return answer
	# absolute the negative values
	return helper(abs(n), ans)


if __name__ == '__main__':
	main()
