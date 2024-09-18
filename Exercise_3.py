class ListNode:
    """
    A node in a singly-linked list.
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None
        self.tail = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        newNode = ListNode(data)
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr:
            if curr.data == key:
                return curr.data
            curr = curr.next
        return None

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        prev = self.head
        while prev and prev.next:
            curr = prev.next
            if curr.data == key:
                prev.next = curr.next

        print()


    def getLinkedList(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next


SinglyLLObj = SinglyLinkedList()
SinglyLLObj.remove(3)
SinglyLLObj.append(1)
SinglyLLObj.append(2)
SinglyLLObj.getLinkedList()
SinglyLLObj.remove(3)
