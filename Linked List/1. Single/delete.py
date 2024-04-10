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
    
    def push(self, x):
        p = Node()
        p.set_data(x)

        if self.__head == None:
            self.__head = p
        else:
            q = self.__head
            while q.get_next() is not None:
                q = q.get_next()
            q.set_next(p) 
        print("node added at head")
    
    def list_nodes(self):
        if self.__head == None:
            print("\nlist is empty\n")
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
    def delete_first_node(self):
        q = self.__head
        temp = 0
        if q is None:
            print("\nlist is empty\n")
        else:
            if q.get_next() is None:
                temp = q.get_data()
                q.set_next(None)
                self.__head = None
                print("\nfirst node as last", temp, "is deleted\n")
            else:
                self.__head = q.get_next()
                temp = q.get_data()
                q.set_next(None)
                print("\nfirst node", temp, "is deleted\n")

    def delete_last_node(self):
        q = self.__head
        temp = 0
        if q is None:
            print("\nlist is empty\n")
        else:
            if q.get_next() is None:
                temp = q.get_data()
                self.__head = None
                print("\nlast node as first", temp, "is deleted\n")
            else:
                while q.get_next().get_next() is not None:
                    q = q.get_next()
                temp = q.get_next().get_data()
                q.set_next(None)
                print("\nlast node", temp, "is deleted\n")

    def delete_specific_value(self, value):
        q = self.__head
        if q is None:
            print("list is empty")
        else:
            if q.get_next() is None:
                self.__head = None
                print("\n", value, "is delete from the list as atmost value\n")

            else:
                p = q
                fisrt = False
                while q.get_next() is not None:
                    if q.get_data() is value:
                        fisrt = True
                        break
                    else:
                        p = q
                        q = q.get_next()
                if fisrt:
                    self.__head = p.get_next()
                    p.set_next(None)
                else:
                    p.set_next(q.get_next())
                    q.set_next(None)
                print("\n", value, "is delete from the list\n")
        
       


sll = SingleLinledList()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.push(50)


while True:
    print("--------MENU--------")
    print("1.list nodes \n2.delete at head \n3.delete at tail \n4.delete a value \n5.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll.list_nodes()
    elif op == 2:
        sll.delete_first_node()
    elif op == 3:
        sll.delete_last_node()
    elif op == 4:
        print("\nenter the value to delete:", end='')
        data = int(input())
        sll.delete_specific_value(data)
    else:
        break
