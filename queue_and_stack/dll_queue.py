import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Queues, like the name suggests, follow the First-in-First-Out (FIFO) principle.
# As if waiting in a queue for the movie tickets,
# the first one to stand in line is the first one to buy a ticket and enjoy the movie.

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    # enqueue() : Adds element to the back of Queue.
    def enqueue(self, value):
        pass

    # dequeue() : Removes and returns the first element from the queue.
    def dequeue(self):
        pass

    # len returns the number of items in the queue.
    def len(self):
        pass
