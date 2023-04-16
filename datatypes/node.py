class Node:

    def __init__(self, object, reference):
        self.data = object
        self.next_node = reference


    def __repr__(self):
        return f"{self.__class__.__name__}(object={self.data}, next_node={self.next_node})"