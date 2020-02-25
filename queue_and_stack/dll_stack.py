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
        self.storage = DoublyLinkedList()

    # push : adds to front of a list
    def push(self, value):
        self.storage.add_to_head(value)

    # pop(): removes and returns last value from the list or the given index value.
    def pop(self):
        if self.storage.head:
            return self.storage.remove_from_head()
        else:
            print("nothing here cannot pop()")
            return None


    # len returns the number of items in the queue.
    def len(self):
        return self.storage.length
