"""
File: subsets.py
Name:
-------------------------
This file prints all the sub-lists on Console
by calling a recursive function - list_sub_lists(lst).
subsets.py is a famous LeetCode Medium problem
"""


def main():
    """
    LeetCode Medium Problem
    """
    list_sub_lists([1, 2, 3, 4])

def dfs(lst, index, subset):
    if index == len(lst):
        print(subset)
        return
    subset.append(lst[index])
    dfs(lst, index + 1, subset)
    subset.pop()
    dfs(lst, index + 1, subset)


def list_sub_lists(lst):
    """
    :param lst: list[str], containing a number of characters
    """
    dfs(lst, 0, [])




if __name__ == '__main__':
    main()
