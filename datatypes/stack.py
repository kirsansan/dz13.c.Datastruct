from datatypes.node import Node


class Stack:

    def __init__(self):
        self.length: int = 0
        self.top = None

    def push(self, object):
        """Push a new object Node-type to the stack"""
        if self.length == 0:
            self.top = Node(object, None)
        else:
            tmp_node: Node = Node(object, self.top)
            self.top = tmp_node
        self.length += 1

    def pop(self):
        """Pop the data
            hope __del__() for old Node will be called automatically
        """
        if self.length > 0:
            self.length -= 1
            tmp_data = self.top.data
            self.top = self.top.next_node
            return tmp_data

    def __len__(self):
        """just return the length (polymorphism does matter)"""
        return self.length
