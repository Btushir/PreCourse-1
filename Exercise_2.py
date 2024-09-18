"""
Stack is a type of LIFO (Last in First Out) data structure meaning element
    added at the end of stack is processed first. There are multiple operations that can be performed on the stack.
    (1) push element to stack (2) pop element from stack (3) peek element from stack (4) get size of stack and more.
    This program implement stack using Linked List and perform operations such as push, pop. Edge cases: (1) pop
     while stack is empty.

    Time complexity: push: O(1) since adding to the start of LL, pop: O(1) since first element is removed

    Space complexity: O(n) that is size of stack

    Did this code successfully run on Leetcode : Yes

    Any problem you faced while coding this :
    There is no need to keep track of tail. The elements can be added at head and popped from the head only.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if self.head:
            popedVal = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popedVal

        return -1


a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
