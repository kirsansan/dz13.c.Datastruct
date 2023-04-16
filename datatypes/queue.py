from datatypes.node import Node

class Queue:


    def __init__(self):
        self.length: int = 0
        self.head = None
        self.tail = None


    def add(self, object):
        """add a new object Node-type to the tail"""
        tmp_node: Node = Node(object, None)
        if self.length == 0:
            self.head = tmp_node
        else:
            self.tail.next_node = tmp_node
        self.tail = tmp_node
        self.length += 1



    def remove(self):
        """remove the data from the head of Queue
            hope __del__() for old Node will be called automatically
        """
        if self.length > 0:
            tmp_data = self.head.data
            self.head = self.head.next_node
            self.length -= 1
            return tmp_data

    def __len__(self):
        """just return the length (polymorphism does matter)"""
        return self.length
