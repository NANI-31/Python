class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
    
    def set_data(self,data):
        self.__data= data
    def get_data(self):
        return self.__data
    
    def set_next(self, next):
        self.__next = next
    def get_next(self):
        return self.__next
    
class Stack:
    def __init__(self):
        self.__top = None
    
    