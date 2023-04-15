from datatypes.node import Node
from datatypes.stack import Stack

if __name__ == '__main__':

    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)
    print(n2.data)
    print(n1)
    print(n2)
    print(n2.next_node)