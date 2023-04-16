from datatypes.node import Node
from datatypes.stack import Stack
from datatypes.queue import Queue
from datatypes.linkedlist import LinkedList

if __name__ == '__main__':

# node types
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)
    print(n2.data)
    print(n1)
    print(n2)
    print(n2.next_node, "\n")

# stack types
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
    print("\n")

# queue types
    queue = Queue()
    queue.add('queue1')
    queue.add('queue2')
    queue.add('queue3')
    print("current length of queue is ", len(queue))
    for _ in range(0, 4):
        print("remove result is ", queue.remove())
    print("\n")

# linked list types
    llist = LinkedList()
    llist.add_to_tail('llist1')
    llist.add_to_tail({"name": "somedata2", "value": "somevalue2"})
    llist.add_to_head('llist0')
    print(llist)
    print("current length of linked_list is ", len(llist))
