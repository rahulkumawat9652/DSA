class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val,end=" ")
                current = current.next
            print()
sll = SinglyLinkedList()
sll.append(10)
sll.traverse()