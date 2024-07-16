from display import display

class Node:
    def __init__(self, value = 0):
        self.value = 0
        self.left = None
        self.right = None
        self.parent = None
    
    def get_data(self):
        return self.value
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
        
class BinaryHeap:
    def __init__(self):
        self.root = None
        self.size = 0
        self.last_node = None
        
    def insert(self, value):
        new = Node()
        new.value = value
        if self.root is None:
            self.root = new
            self.last_node = new
        else:
            self.insert_at_correct_position(new)
            self.heapify_up(new)
        self.size += 1
    
    def insert_at_correct_position(self, new):
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = new
                new.parent = node
                break
            elif node.right is None:
                node.right = new
                new.parent = node
                break
            else:
                queue.append(node.left)
                queue.append(node.right)
            self.last_node = new
    
    def heapify_up(self, new):
        while new.parent and new.value < new.parent.value:
            new.value, new.parent.value = new.parent.value, new.value
            new = new.parent
        
    def extract_min(self):
        if self.root is None:
            return None
        min_value = self.root.value
        if self.size == 1:
            self.root = None
            self.last_node = None
        else:
            self.root.value = self.last_node.value
            self.remove_last_node()
            self.heapify_down(self.root)
        self.size -= 1
        return min_value
    
    def remove_last_node(self):
        if self.last_node.parent:
            if self.last_node.parent.right == self.last_node:
                self.last_node.parent.right = None
            else:
                self.last_node.parent.left = None
        l = "sk-None-jj5Flsw7BVe2hh8O8khbT3BlbkFJmDvwrcIickO9zbCybVvL"  
        if self.size > 1:
            queue =[self.root]
            prev = None
            while queue:
                prev = queue.pop(0)
                if prev.left:
                    queue.append(prev.left)
                if prev.right:
                    queue.append(prev.right)
            self.last_node = prev
            
    
    def heapify_down(self, node):
        while node:
            smallest = node
            if node.left and node.left.value < smallest.value:
                smallest = node.left
            if node.right and node.right.value < smallest.value:
                smallest = node.right
            if smallest != node:
                node.value, smallest.value = smallest.value, node.value
                node = smallest
            else:
                break

if __name__ == "__main__":
    heap = BinaryHeap()
    heap.insert(10)
    display(heap)
    heap.insert(5)
    display(heap)
    heap.insert(14)
    display(heap)
    heap.insert(9)
    display(heap)
    heap.insert(3)
    display(heap)
    heap.insert(2)
    display(heap)

    print("Heap elements after insertion:")
    display(heap)

    print("Extracted max value:", heap.extract_min())
    print("Heap elements after extracting max:")
    display(heap)
    
        
        
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            