class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
        self.__prev_next = None

    def set_data(self,data):
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_prev_next(self,data):
        self.__prev_next = data
    def get_prev_next(self):
        return self.__prev_next
    
    def set_next(self,data):
        self.__next = data
    def get_next(self):
        return self.__next
    
class DoubleLinledList:
    def __init__(self):
        self.__head = None
    
    def add_at_tail(self, x):
        p = Node()
        p.set_data(x)

        if self.__head == None:
            self.__head = p
        else:
            q = self.__head
            while q.get_next() is not None:
                q = q.get_next()
            q.set_next(p) 
            p.set_prev_next(q)
        print("node added at tail\n")
        
    def add_at_head(self, x):
        p = Node()
        p.set_data(x)

        if self.__head == None:
            self.__head = p
        else:
            q = self.__head
            p.set_next(q)
            q.set_prev_next(p)
            self.__head = p
            h = self.__head
            # print(h.get_next().get_prev_next().get_data())
        print("node added at head\n")
    
    def list_nodes(self):
        if self.__head == None:
            print("list is empty\n")
        else:
            q = self.__head
            first_node = True  # Flag to track the last node
            while q is not None:
                if not first_node:
                    print(" <=> ", end='')  # Print '->' for all nodes except the last one
                print(q.get_data(), end='')
                first_node = False
                q = q.get_next()
            print('\n')
    def print_middle_values(self):
        l =[]
        q = self.__head
        if q != None:
            if q.get_next() is None:
                print(q.get_data())
            else:
                while q is not None:
                    l.append(q.get_data())
                    q = q.get_next()
                m = len(l) // 2
                print("\nthe middel value(S) are:", end=" ")
                # print((l[m], l[m+1]) if len(l) == 2 else (l[m],) if len(l) % 2 == 0 else l[m])
                if len(l) == 2:
                    print(l[0],",",l[1],"\n")
                else:
                    print((l[m-1], l[m]) if len(l) % 2 == 0 else (l[m]))
                    print()
        else:
            print("the list is empty\n")
        
    def add_at_position(self, data, pos):
        if pos == 1:
            self.add_at_head(data)
        else:
            neew = Node()
            neew.set_data(data)
            q = self.__head
            prev = q
            c = 1
            while q.get_next() is not None:
                if pos == c:
                    break
                else:
                    prev = q
                    q = q.get_next()
                    c += 1
            neew.set_prev_next(q.get_prev_next())
            neew.set_next(prev.get_next())
            prev.set_next(neew)
            q.set_prev_next(neew)
            print("node added at postion\n")
       


sll = DoubleLinledList()

while True:
    print("--------MENU--------")
    print("1.add at tail \n2.add at head \n3.Add in position(btw) \n4.list nodes \n5.middle values \n6.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print("\nenter the data:", end=" ")
        data = int(input())
        sll.add_at_tail(data)
    elif op == 2:
        print("\nenter the data:", end=" ")
        data = int(input())
        sll.add_at_head(data)
    elif op == 3:
        print("\nenter the data:", end=" ")
        data = int(input())
        print("enter the position:", end=" ")
        pos = int(input())
        sll.add_at_position(data, pos) 
    elif op == 4:
        print()
        sll.list_nodes()
    elif op == 5:
        sll.print_middle_values()
    else:
        break
