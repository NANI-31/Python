class Node:
    def __init__(self):
        self.__value = 0
        self.__next = None
        self.__prev = None
    
    def set_value(self, value):
        self.__value = value
        
    def get_value(self):
        return self.__value

    def set_next(self, next):
        self.__next = next

    def get_next(self):
        return self.__next
        
    def set_prev(self, prev):
        self.__prev = prev
        
    def get_prev(self):
        return self.__prev
    
class Dequeue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def enqueue_front(self, data):
        new  = Node()
        new.set_value(data)
        
        if self.is_empty():
            self.front = self.rear = new
        else:
            new.set_next(self.front)
            self.front.set_prev(new)
            self.front = new
        self.size += 1
        print(f"enqueued {data} to the front of the dequeue\n")
            
    def enqueue_rear(self, data):
        new = Node()
        new.set_value(data)
        
        if self.is_empty():
            self.front = self.rear = new
        else:
            self.rear.set_next(new)
            new.set_prev(self.rear)
            self.rear = new
        self.size += 1
        print(f"enqueued {data} to the rear of the dequeue\n")
        
    def dequeue_front(self):
        if self.is_empty():
            return print("\ndequeue is empty\n")
        d_val = self.front.get_value()
        self.front = self.front.get_next()
        if self.front is None:
            self.rear = None
        else:
            self.front.set_prev(None)
        self.size -= 1
        print(f"\ndequeued {d_val} from the front of the dequeue\n")
    
    def dequeue_rear(self):
        if self.is_empty():
            return print("\ndequeue is empty\n")
        d_val = self.rear.get_value()
        self.rear = self.rear.get_prev()
        if self.rear is None:
            self.front = None
        else:
            self.rear.set_next(None)
        self.size -= 1
        print(f"\ndequeues {d_val} from the rear of the dequeue\n")
    
    def peek_front(self):
        if self.is_empty():
            print("\ndeque is empty. Cannot peek front\n")
            return None
        print(f"\nfront of the deque is {self.front.get_value()}\n")
        return self.front.get_value()

    def peek_rear(self):
        if self.is_empty():
            print("\ndeque is empty. Cannot peek rear\n")
            return None
        print(f"\nrear of the deque is {self.rear.get_value()}\n")
        return self.rear.get_value()

    def is_empty(self):
        return self.front is None

    def get_size(self):
        size = self.size
        print(f"\ndeque size is {size}\n")
        return size

    def display(self):
        if self.is_empty():
            print("\ndeque is empty\n")
            return
        current = self.front
        print("\ndeque values:")
        while current:
            print(current.get_value(), end=" ")
            current = current.get_next()
        print()


dequeue = Dequeue()

while True:
    print("------dequeue MENU------\n1.enqueue front\n2.enqueue rear\n3.dequeue front\n4.dequeue rear\n5.peek front\n6.peek rear\n7.dequeue size\n8.display")
    op = int(input("enter the choice: "))
    if op == 1:
        data = int(input("\nenter the data: "))
        dequeue.enqueue_front(data)
    elif op == 2:    
        data = int(input("\nenter the data: "))
        dequeue.enqueue_rear(data)
    elif op == 3:
        dequeue.dequeue_front()    
    elif op == 4:    
        dequeue.dequeue_rear()
    elif op == 5:    
        dequeue.peek_front()
    elif op == 6:    
        dequeue.peek_rear()
    elif op == 7:    
        dequeue.get_size()
    elif op == 8:
        dequeue.display()
    else:
        break    
        