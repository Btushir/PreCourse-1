class myStack:
    #Please read sample.java file before starting.
    #Kindly include Time and Space complexity at top of each file

    """
    Stack is a type of LIFO (Last in First Out) data structure meaning element
    added at the end of stack is processed first. There are multiple operations that can be performed on the stack.
    (1) push element to stack (2) pop element from stack (3) peek element from stack (4) get size of stack and more.
    This program implement stack using array and perform operations such as push, pop, peek, get size of stack,
    print stack. Edge cases: (1) pop while stack is empty.
    Time complexity: push: O(1) since adding to the last of array, pop: O(1) since last element is removed peek: O(1),
    isEmpty: O(1), size: O(1) and show(): O(n) since need to traverse the whole array.

    Space complexity: O(n) that is size of stack

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
        self.stack = []

    def isEmpty(self):
        if self.stack:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack


s = myStack()
s.push('1')
s.push('2')
print(f"size of the stack is: {s.size()}")
print(s.pop())
print(f"size of the stack is: {s.size()}")
print(f"stack is: {s.show()}")
