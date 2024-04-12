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
            q = self.__head
            first_node = True  # Flag to track the last node
            while q is not None:
                if not first_node:
                    print(" -> ", end='')  # Print '->' for all nodes except the last one
                print(q.get_data(), end='')
                first_node = False
                q = q.get_next()
            print('\n')
            
    def merge_nodes(self, list1, list2):
        list1_curr = list1.__head 
        list2_curr = list2.__head 
  
        # swap their positions until one finishes off 
        while list1_curr != None and list2_curr != None: 
  
            # Save next pointers 
            list1_next = list1_curr.get_next()
            list2_next = list2_curr.get_next()
  
            # make list2_curr as next of list1_curr 
            list2_curr.set_next(list1_next)  # change next pointer of list2_curr 
            list1_curr.set_next(list2_curr)  # change next pointer of list1_curr 
  
            # update current pointers for next iteration 
            list1_curr = list1_next 
            list2_curr = list2_next 
            list2.__head = list2_curr
        

            


sll1 = SingleLinledList()
sll2 = SingleLinledList()
sll1.push(1) 
sll1.push(2) 
sll1.push(3) 
sll1.push(4) 
sll1.push(5) 
sll1.push(6) 
for i in range(11, 15,): 
    sll2.push(i) 



while True:
    print("--------MENU--------")
    print("1.list nodes \n2.list nodes \n3.list nodes \n4.Merge Lists \n5.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll1.list_nodes()
    elif op == 2:
        print()
        sll1.list_nodes()
    elif op == 3:
        print()
        sll2.list_nodes()
    elif op == 4:
        print()
        sll1.merge_nodes(sll1, sll2)
    else:
        break
