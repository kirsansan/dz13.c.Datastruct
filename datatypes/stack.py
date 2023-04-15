from datatypes.node import Node

class Stack:
    length: int = 0
    top = None


    def push(self, object):
        if Stack.length == 0:
            self.node: Node = Node(object, None)
            Stack.top = self.node
        else:
            self.node :Node = Node(object, Stack.top)
        Stack.length += 1
        Stack.top = self.node


    # def pop(self):
    #     ...