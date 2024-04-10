class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None

    def set_data(self,data):
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_next(self,data):
        self.__next = data
    def get_next(self):
        return self.__next
    
class SingleLinledList:
    def __init__(self):
        self.__head = None
    
    def add_at_head(self, x):
        p = Node()
        p.set_data(x)

        if self.__head == None:
            self.__head = p
        else:
            q = self.__head
            while q.get_next() is not None:
                q = q.get_next()
            q.set_next(p) 
        print("node added at head\n")
    
    def list_nodes(self):
        if self.__head == None:
            print("list is empty")
        else:
            q = self.__head
            first_node = True  # Flag to track the last node
            while q is not None:
                if not first_node:
                    print(" -> ", end='')  # Print '->' for all nodes except the last one
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
                    print((l[m], l[m+1]) if len(l) % 2 == 0 else (l[m]))
                    print()
        else:
            print("the list is empty\n")
        
    def add_at_position(self, pos):
        q = self.__head
        p = q
        c = 0
        while q.get_next() is not None:
            if pos == c-1:
                break
            else:
                p = q
                q = q.get_next()
                c += 1
            pass
       


sll = SingleLinledList()

while True:
    print("--------MENU--------")
    print("1.add at head \n2.list nodes \n3.middle values \n4.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print("\nenter the data:", end=" ")
        data = int(input())
        sll.add_at_head(data)
    elif op == 2:
        print()
        sll.list_nodes()
    elif op == 3:
        sll.print_middle_values()
    else:
        break
