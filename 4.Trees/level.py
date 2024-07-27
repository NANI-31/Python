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
            
   

    def level(self, data):
        level, found = self.level_recursive(self.root, data)
        print(level) if found else print("no data found")
    def level_recursive(self, cur_node, data):
        if cur_node is None: return 0, False
        if cur_node.get_data() == data: return 1, True
        
        elif cur_node.get_data() > data:
            lNode, f = self.level_recursive(cur_node.get_left(), data)
            
            if f: return lNode+1, True
        
        else:
            rNode, f = self.level_recursive(cur_node.get_right(), data)
            
            if f: return rNode+1, True
        
        return 0, False        
    
    def getLevelUtil(self, node, data, level):
        if (node == None): return 0
        if (node.get_data() == data): return level
        
        downlevel = self.getLevelUtil(node.get_left(),data, level + 1)
        
        if (downlevel != 0): return downlevel
        
        downlevel = self.getLevelUtil(node.get_right(),data, level + 1)
        return downlevel
  
    def getLevel(self, data):
        return self.getLevelUtil(self.root, data, 1)
    
            
if __name__ == "__main__":
    bt = Tree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(6)
    bt.insert(7)
    display(bt)
    bt.level(8)
            
            
                 