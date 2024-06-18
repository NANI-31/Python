class Dequeue:
    def __init__(self):
        self.dequeue = []
    

        
    def enqueue_front(self, data):
        self.dequeue.append(data)
        print(f"added {data} to the front of the deque.\n")
        
    def enqueue_rearr(self, data):
        self.dequeue.insert(0, data)
        print(f"added {data} to the rare of the deque.\n")
        
    def dequeue_rearr(self):
        if self.isEmpty():
            return print("\ndequeue is empty cannot remove rear\n")
        d_rear = self.dequeue.pop()
        print(f"\ndequeued {d_rear} from the rear\n")

    def dequeue_front(self):
        if self.isEmpty():
            print("\ndequeue is empty cannot remove front\n")
            return None
        d_rear = self.dequeue.pop(0)
        print(f"\ndequeued {d_rear} from the front\n")
        
    def peek_front(self):
        if self.isEmpty():
            return print("\ndequeue is empty cannot peek\n")
        print(f"\nfront of the dequeue is {self.dequeue[0]}\n")

    def peek_rearr(self):
        if self.isEmpty():
            return print("dequeue is empty cannot peek")
        print(f"\nrear of the dequeue is {self.dequeue[-1]}\n")
        
    def get_size(self):
        size = len(self.dequeue)
        print(f"\ndequeue size is {size}\n")
            
    def display(self):
        if self.isEmpty():
            print("\ndequeue is empty\n")
            return
        print(self.dequeue, end=" ")
        
    def isEmpty(self):
        return len(self.dequeue) == 0

dequeue = Dequeue()
while True:
    print("------dequeue MENU------\n1.enqueue front\n2.enqueue rear\n3.dequeue front\n4.dequeue rear\n5.peek front\n6.peek rear\n7.dequeue size\n8.display")
    op = int(input("enter the choice: "))
    if op == 1:
        data = int(input("\nenter the data: "))
        dequeue.enqueue_front(data)
    elif op == 2:    
        data = int(input("\nenter the data: "))
        dequeue.enqueue_rearr(data)
    elif op == 3:
        dequeue.dequeue_front()    
    elif op == 4:    
        dequeue.dequeue_rearr()
    elif op == 5:    
        dequeue.peek_front()
    elif op == 6:    
        dequeue.peek_rearr()
    elif op == 7:    
        dequeue.get_size()
    elif op == 8:
        dequeue.display()
    else:
        break    