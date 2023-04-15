from datatypes.node import Node

class Stack:
    length: int = 0
    top = None


    def push(self, object):
        """Push a new object Node-type to the stack"""
        if Stack.length == 0:
            self.node: Node = Node(object, None)
            Stack.top = self.node
        else:
            self.node: Node = Node(object, Stack.top)
        Stack.length += 1
        Stack.top = self.node


    def pop(self):
        """Pop the data
            hope __del__() for old Node will be called automatically
        """
        if Stack.length > 0:
            Stack.length -= 1
            tmp_data = Stack.top.data
            Stack.top = Stack.top.next_node
            return tmp_data
