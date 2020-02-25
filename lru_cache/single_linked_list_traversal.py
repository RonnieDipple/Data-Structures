class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def add(self, value):
        self.next = Node(value)

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node


    def printMiddle(self):
        slow = self.head
        fast = self.head

        if self.head is not None:
            while(fast is not None and fast.next is not None):
                fast = fast.next.next
                slow = slow.next
            return slow.data




    # Break out groups answer
    #
    # class Node:
    #     def __init__(self, value):
    #         self.value = value
    #         self.next = None
    #
    #     def add(self, value):
    #         self.next = Node(value)
    #
    # class LinkedList:
    #     def __init__(self, node=None):
    #         self.head = node
    #         self.tail = node
    #
    #     def push(self, value):
    #         new_node = Node(value)
    #         self.tail.next = new_node
    #         self.tail = new_node
    #
    #     def find_middle(self):
    #         # traverse the loop two nodes at a time
    #         hare = self.head
    #         tortoise = self.head
    #         if self.head is None:
    #             return None
    #         while hare is not None:
    #             hare = hare.next.next
    #             # the tortoise travels one node at a time
    #             tortoise = tortoise.next
    #         # when the hare reaches the end, return the node the tortoise is on
    #         return tortoise

    # reversing a linked list
    # function reverse(head) {
    # // Step 1
    #   let previous = null
    #   let current = head
    #   let following = head
    # // Step 2
    #   while(current !== null) {
    #     following = following.next
    #     current.next = previous
    #     previous = current
    #     current = following
    #   }
    # // Step 3
    #   return previous
    # }
