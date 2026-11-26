class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def cycle(self):
        temp = self.head
        travel = 0
        my_dict = dict()
        while temp is not None:
            if temp in my_dict:
                return travel - my_dict[temp]
            my_dict[temp] = travel
            travel += 1
            temp = temp.next
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