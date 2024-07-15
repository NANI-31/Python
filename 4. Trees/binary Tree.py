from display import display
import time

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
        self.preorder_recursive(self.root, result)
        print("preorder traversal: ",result)
    def preorder_recursive(self, node, result):
        if node:
            result.append(node.get_data())
            self.preorder_recursive(node.get_left(), result)
            self.preorder_recursive(node.get_right(), result)
            
    # ----------------postorder-----------------
    def postorder_traversal(self):
        result = []
        self.postorder_recursive(self.root, result)
        print("postorder traversal: ",result)
    def postorder_recursive(self, node, result):
        if node:
            self.postorder_recursive(node.get_left(), result)
            self.postorder_recursive(node.get_right(), result)
            result.append(node.get_data())
            
    def search(self, data):
        return self.search_recursive(self.root, data)
    
    def search_recursive(self, cur_node, data):
        if cur_node is None or cur_node.get_data() == data:
            return cur_node
        elif data < cur_node.get_data():
            return self.search_recursive(cur_node.get_left(), data)
        else:
            return self.search_recursive(cur_node.get_right(), data)
    
    def level(self, data):
        level, found = self.level_recursive(self.root, data)
        print(level) if found else print("no data found")
    def level_recursive(self, cur_node, data):
        if cur_node is None:
            return 0, False
        if cur_node.get_data() == data:
            return 1, True
        elif cur_node.get_data() > data:
            lNode, f = self.level_recursive(cur_node.get_left(), data)
            if f:
                return lNode+1, True
        else:
            rNode, f = self.level_recursive(cur_node.get_right(), data)
            if f:
                return rNode+1, True
        return 0, False        
    
    def getLevelUtil(self, node, data, level):
        if (node == None):
            return 0
     
        if (node.get_data() == data):
            return level
     
        downlevel = self.getLevelUtil(node.get_left(),
                                 data, level + 1)
        if (downlevel != 0):
            return downlevel
     
        downlevel = self.getLevelUtil(node.get_right(),
                                 data, level + 1)
        return downlevel
 
# Returns level of given data value
 
 
    def getLevel(self, data):
 
        return self.getLevelUtil(self.root, data, 1)
    
    def size_tree(self):
        print(self.size_recursive(self.root))
    def size_recursive(self, node):
        if node is None:
            return 0
        else:
            return (self.size_recursive(node.get_left()) + 1 + self.size_recursive(node.get_right()))
            
    def height_tree(self):
        print(self.height_recursive(self.root))
    def height_recursive(self, node):
        if node is None:
            return 0
        else:
            lDepth = self.height_recursive(node.get_left())
            rDepth = self.height_recursive(node.get_right())
            
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1
            # return max(lDepth, rDepth) + 1
            
if __name__ == "__main__":
    bt = Tree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(6)
    bt.insert(7)
    bt.inorder_traversal()
    bt.preorder_traversal()
    bt.postorder_traversal()
    display(bt)
    bt.size_tree()
    bt.height_tree()
    bt.level(8)
    # print("size of the tree is: ",bt.size_tree())
    node_value = 7
    
    start = time.time()
    bt.level(node_value)
    end = time.time()
    print(end-start)
    
    start = time.time()
    print(bt.getLevel(node_value))
    end = time.time()
    print(end-start)
        
            
            
                 