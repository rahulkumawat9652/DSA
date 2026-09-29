class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current
obj = LinkedList()
obj.insert_at(100, 0)
obj.insert_at(102, 1)
obj.insert_at(103, 2)
current = obj.head
while current is not None:
    print(current.data)
    current = current.next