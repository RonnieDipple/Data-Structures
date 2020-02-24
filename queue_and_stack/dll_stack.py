import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Stacks, like the name suggests, follow the Last-in-First-Out (LIFO) principle.
# As if stacking coins one on top of the other,
# the last coin we put on the top is the one that is the first to be removed
# from the stack later.


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    # push : adds to front of a list
    def push(self, value):
        pass

    # pop(): removes and returns last value from the list or the given index value.
    def pop(self):
        pass

    # len returns the number of items in the queue.
    def len(self):
        pass
