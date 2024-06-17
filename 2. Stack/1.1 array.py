class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"Pushed {value} onto the stack.")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_value = self.stack.pop()
        print(f"Popped {popped_value} from the stack.")
        return popped_value

    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Cannot peek.")
            return None
        top_value = self.stack[-1]
        print(f"Top of the stack is {top_value}.")
        return top_value

    def isEmpty(self):
        return len(self.stack) == 0

    def getSize(self):
        size = len(self.stack)
        print(f"Stack size is {size}.", size)
        return size

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    stack.pop()
    stack.peek()
    stack.getSize()
    stack.pop()
    stack.pop()
    stack.pop()
