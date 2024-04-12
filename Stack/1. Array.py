maxSize = 10
top = -1
stack = [0] * maxSize

def isFull():
    if top == maxSize:
        return 1
    else:
        return 0
    
def push(data):
    global top
    if isFull() != 1:
        top += 1
        stack[top] = data
    else:
        print("Could not insert data, Stack is full.")
    return data

push(44)
push(10)
push(62)
push(123)
push(15)

print("Stack Elements: ")
for i in range(maxSize):
    print(stack[i], end = " ")