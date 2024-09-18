class MyStack:
    """
    Stack is a type of LIFO (Last in First Out) data structure meaning element
    added at the end of stack is processed first. There are multiple operations that can be performed on the stack.
    (1) push element to stack (2) pop element from stack (3) peek element from stack (4) get size of stack and more.
    This program implement stack using array and perform operations such as push, pop, peek, get size of stack,
    print stack. Edge cases: (1) pop while stack is empty.
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :
    I got into one error while solving it on leetcode: when incrementing the stack item by some value:
    I used this:
         for item in stack:
              item += value
    corrected code:
        for idx in range(len(stack)):
            stack[idx] += value

    The problem with first code is that it is updating the item variable not the value in stack,
    so we need to change the value at index
    """

    def __init__(self):
        """
        Constructor of the class MyStack, called when an object of the class is created.
        """
        self.stack = []

    def isEmpty(self):
        """
        This is a method to check if the stack is empty
        Parameters:
            None
        Returns:
            None
        Example:
            stack = MyStack()
            stack.isEmpty() # Return True if stack is empty
        TC: O(1)
        """
        if self.stack:
            return True
        return False

    def push(self, item):
        """
        This is method to push an element into stack.
        Parameters:
            item: element to be pushed into stack
        Returns:
            None
        Example:
            stack = MyStack()
            stack.push()
        TC: O(1) since stack is implemented using array
        """
        self.stack.append(item)

    def pop(self):
        """
        This is method to pop an element from stack.
        Parameters:
            None
        Returns:
            the popped element from stack
        Example:
            stack = MyStack()
            stack.pop()
        TC: O(1) since stack is implemented using array
        """
        if self.stack:
            return self.stack.pop()
        return -1

    def peek(self):
        """
        This is method to peek an element from stack.
        Parameters:
            None
        Returns:
            the top element from stack
        Example:
            stack = MyStack()
            stack.peek()
        TC: O(1) since stack is implemented using array

        """
        return self.stack[-1]

    def size(self):
        """
        This is method to return the size of stack
        Parameters:
            None
        Returns:
            the length of stack
        Example:
            stack = MyStack()
            stack.size()
        TC: O(1) since stack is implemented using array

        """
        return len(self.stack)

    def show(self):
        """
        This is method to print the stack.
        Parameters:
            None
        Returns:
            current stack
        Example:
            stack = MyStack()
            stack.show()
        TC: O(n) since need to traverse the stack
        """
        return self.stack


s = MyStack()
s.push('1')
s.push('2')
print(f"size of the stack is: {s.size()}")
print(s.pop())
print(f"size of the stack is: {s.size()}")
print(f"stack is: {s.show()}")
