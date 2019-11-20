class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self, head, data):
            p = Node(data)
            if head is None:
                head = p
            elif head.next is None:
                head.next = p
            else:
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
        if head is None or head.next is None:
            return head
        if head.data == head.next.data:
            head.next = head.next.next
            self.removeDuplicates(head)
        else:
            self.removeDuplicates(head.next)
        return head


if __name__ == '__main__':
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    head = mylist.removeDuplicates(head)
    mylist.display(head)
