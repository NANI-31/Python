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
        print("node added at head\n")
    
    def list_nodes(self):
        if self.__head == None:
            print("\nlist is empty\n")
        else:
            temp = self.__head
            while(temp):
                print(temp.get_data(), end=" ")
                temp = temp.get_next()
            print('\n')




    def reversed_list(self):
        q = self.__head
        prev = None
        while q is not None:
            next = q.get_next()
            q.get_next = prev
            prev = q
            q = next
        self.__head = prev



        
       


sll = SingleLinledList()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.push(50)


while True:
    print("--------MENU--------")
    print("1.list nodes \n2.reverse values \n3.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll.list_nodes()
    elif op == 2:
        sll.reversed_list()
    else:
        break
