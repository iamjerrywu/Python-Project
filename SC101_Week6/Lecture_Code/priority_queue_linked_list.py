"""
File: priority_queue_linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It controls the condition to break the input loop
EXIT = ''


class ListNode:
	def __init__(self, val, next_one):
		self.val = val
		self.next = next_one


def main():
	priority_queue = None
	while True:
		name = input(f'Name of patient ({EXIT} to quit): ')
		if name == EXIT:
			break
		priority = int(input('Priority: '))
		data = (name, priority)
		if priority_queue is None:
			priority_queue = ListNode(data, None)
		else:
			if priority_queue.val[1] > priority:
				# New node at the beginning
				new = ListNode(data, priority_queue)
				priority_queue = new

			else:
				# New node in between
				cur = priority_queue
				prev = priority_queue
				while cur and priority >= cur.val[1]:
					prev = cur
					cur = cur.next
				if cur:
					# in between
					new = ListNode(data, cur)
				else:
					# new node is end node
					new = ListNode(data, None)
				prev.next = new
	while priority_queue:
		print(priority_queue.val)
		priority_queue = priority_queue.next


if __name__ == '__main__':
	main()
