from display import display

class Node:
    def __init__(self):
        self.__data = 0 
        self.__right = None
        self.__left = None
    
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_right(self, right):
        self.__right = right
    def get_right(self):
        return self.__right
    
    def set_left(self, left):
        self.__left = left
    def get_left(self):
        return self.__left
        

class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        q = Node()
        q.set_data(data)
        if self.root is None:
            self.root = q
        else:
            self.insert_recursive(self.root, data)
        
    def insert_recursive(self, curr_node, data):
        q = Node()
        q.set_data(data)
        
        if curr_node.get_data() > data:
            if curr_node.get_left() is None:
                curr_node.set_left(q)
            else:
                self.insert_recursive(curr_node.get_left(), data)
        elif curr_node.get_data() < data:
            if curr_node.get_right() is None:
                curr_node.set_right(q)
            else:
                self.insert_recursive(curr_node.get_right(), data)
        
        else:
            print(f"data {data} is already exists in the tree")
            
    def delete(self, data):
        self.root = self.delete_recursive(self.root, data)
    
    def delete_recursive(self, curr_node, data):
        
        if curr_node.get_data() > data:
            self.delete_recursive(curr_node.get_left())   
        elif curr_node.get_data() < data:
            self.delete_recursive(curr_node.get_right())
        else:
            # case 1: node has no children
            if curr_node.get_left() is None and curr_node.get() is None:
                return None
            
            # case 2: node has one child
            if curr_node.get_left() is None:
                return curr_node.get_right()   
            if curr_node.get_right() is None:
                return curr_node.get_left()
            
            # case 3: node has two child
            
            successor = self.find_min_val(curr_node.get_right())
            curr_node.set_data(successor.get_data())
            curr_node.set_right(self.delete_recursive(curr_node.get_right, successor.get_data()))
        
        return curr_node
    
    def find_min_val(self, data):
        curr = data
        while curr.get_left() is not None:
            cur = cur.get_left()
        return curr
    
    # ----------------inorder----------------
    def inorder_traversal(self):
        result = []
        self.inorder_recursive(self.root, result)
        print("inorder traversal: ",result)
    def inorder_recursive(self, node, result):
        if node:
            self.inorder_recursive(node.get_left(), result)
            result.append(node.get_data())
            self.inorder_recursive(node.get_right(), result)
            
    # ----------------preorder-----------------
    def preorder_traversal(self):
        result = []
        self.inorder_recursive(self.root, result)
        print("inorder traversal: ",result)
    def preorder_recursive(self, node, result):
        if node:
            result.append(node.get_data())
            self.inorder_recursive(node.get_left(), result)
            self.inorder_recursive(node.get_right(), result)
            
    # ----------------postorder-----------------
    def postorder_traversal(self):
        result = []
        self.inorder_recursive(self.root, result)
        print("inorder traversal: ",result)
    def postorder_recursive(self, node, result):
        if node:
            self.inorder_recursive(node.get_left(), result)
            self.inorder_recursive(node.get_right(), result)
            result.append(node.get_data())
            

if __name__ == "__main__":
    bt = Tree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    # bt.insert(5)
    bt.insert(6)
    bt.insert(7)
    bt.inorder_traversal()
    display(bt)
        
            
            
                 