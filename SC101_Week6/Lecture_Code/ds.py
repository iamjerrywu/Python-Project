"""
File: ds.py
Name: Jerry Liao
------------------------------------
This file shows all the data structures
we built today, including Tree, ListNode, and
PriorityQueue with enqueue, dequeue, traversal,
and length methods.
"""


class Tree:
    def __init__(self, left, value, right):
        self.tree_value = value
        self.right = right
        self.left = left


class ListNode:
    def __init__(self, value, next_one):
        self.value = value
        self.next = next_one


class PriorityQueue:

    def __init__(self):
        self.pq = ListNode(None, None)

    def enqueue(self, element):
        if self.pq.value is None:
            self.pq.value = element
        else:
            if self.pq.value[1] > element[1]:
                # New node at the beginning
                new_node = ListNode(element, self.pq)
                self.pq = new_node
            else:
                # New node in between
                current = self.pq
                while current.next is not None:
                    if current.value[1] <= element[1] < current.next.value[1]:
                        new_node = ListNode(element, current.next)
                        current.next = new_node
                        break
                    current = current.next
                # New node at the end
                if current.next is None:
                    current.next = ListNode(element, None)

    def dequeue(self):
        element = self.pq
        self.pq = self.pq.next
        return element

    def traversal(self):
        current = self.pq
        while current is not None:
            if current.next is not None:
                print(current.value[0].tree_value, current.value[1], end=', ')
            else:
                print(current.value[0].tree_value, current.value[1])
            current = current.next

    def length(self):
        count = 0
        current = self.pq
        while current is not None:
            count += 1
            current = current.next
        return count
