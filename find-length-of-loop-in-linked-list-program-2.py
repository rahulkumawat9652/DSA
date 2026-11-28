class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0
s1 = SinglyLinkedList()
s1.head = Node(10)
s1.head.next = Node(20)
s1.head.next.next = Node(30)
s1.head.next.next.next = Node(40)
s1.head.next.next.next.next = Node(50)
s1.head.next.next.next.next.next = Node(60)
s1.head.next.next.next.next.next.next = s1.head.next.next #make cycle
print(s1.cycle())