class Node:
    def __init__(self):
        self.__value = 0
        self.__next = None
    
    def set_value(self, value):
        self.__value = value
        
    def get_value(self):
        return self.__value

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next
    
class Cqueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, data):
        new = Node()
        new.set_value(data)
        if self.isEmpty():
            self.front = self.rear = new
            self.rear.set_next(self.front)
        else:
            self.rear.set_next(new)
            #new.set_next(self.front)
            self.rear = new
            self.rear.set_next(self.front)
        self.size += 1
        print(f"Enqueued {data} to the queue.")
        
    def dequeue(self):
        if self.isEmpty():
            return print("\nqueue is empty\n")
        
        value = self.front.get_next()
        if self.front is self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.get_next()
            self.rear.set_next(self.front)
        self.size -= 1
        print(f"\ndequeued {value} from the queue\n")
        
    def peek_front(self):
        if self.is_empty():
            print("\nQueue is empty. Cannot peek front\n")
            return None
        print(f"Front of the queue is {self.front.get_value()}.")


    def peek_rear(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek rear\n")
            return None
        print(f"Rear of the queue is {self.rear.get_value()}.")


    def is_empty(self):
        return self.front is None

    def get_size(self):
        print(f"Queue size is {self.size}.")


    def display(self):
        if self.is_empty():
            return print("Queue is empty")
        print("Queue values:", end=" ")
        current = self.front
        while current is not self.front:
            print(current.get_value(), end=" ")
            current = current.get_next()
        print()

cqueue = Cqueue()
while True:
    print("------circular queue MENU------\n1.enqueue\n2.dequeue\n3.peek\n4.rear\n5.size\n6.display\n7.exit")
    op = int(input("enter your choice:"))
    if op == 1:
        data = int(input("\nenter the data:"))
        cqueue.enqueue(data)
    elif op == 2:
        cqueue.dequeue()
    elif op == 3:
        cqueue.peek_front()
    elif op == 4:
        cqueue.peek_rear()
    elif op == 5:
        cqueue.get_size()
    elif op == 6:
        cqueue.display()
    else:
        break

        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        