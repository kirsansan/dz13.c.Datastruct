from datatypes.node import Node
from datatypes.stack import Stack

if __name__ == '__main__':

    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)
    print(n2.data)
    print(n1)
    print(n2)
    print(n2.next_node, "\n")

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.top.data)
    print(stack.top.next_node.data)
    print(stack.top.next_node.next_node.data)
    print(stack.top.next_node.next_node.next_node)
    #print(stack.top.next_node.next_node.next_node.data)

    for x in range(0, 4):
        print(stack.pop())
