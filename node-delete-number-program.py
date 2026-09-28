def delete(self,val):
    temp = self.head
    if temp.val == val:
        self.head = temp.next
        return
    else:
        found = False
        prev = None
        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next
        if found:
            prev.next = temp.next
            return
        else:
            print("None not found")