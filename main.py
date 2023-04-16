from datatypes.node import Node
from datatypes.stack import Stack
from datatypes.queue import Queue

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

    for _ in range(0, 4):
        print("pop result is ", stack.pop())

    queue = Queue()
    queue.add('queue1')
    queue.add('queue2')
    queue.add('queue3')
    print("current length of queue is ", len(queue))
    for _ in range(0, 4):
        print("remove result is ", queue.remove())
