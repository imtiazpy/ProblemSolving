class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        start = head
        while start.next is not None:
            start = start.next
        start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        if not head:
            return None
        current = head
        while current.next:
            if current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next
        return head



myList = Solution()
T = int(input())
head = None
for _ in range(T):
    data = int(input())
    head = myList.insert(head, data)

head = myList.removeDuplicates(head)
myList.display(head)