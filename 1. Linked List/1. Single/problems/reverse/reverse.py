def reversed_list(self):
    current = self.__head
    if current != None:
        prev = None
        while current is not None:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.__head = prev
    
    else:
        print("the list is empty\n")