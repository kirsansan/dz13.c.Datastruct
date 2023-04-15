from unittest import TestCase

from datatypes.node import Node
from datatypes.stack import Stack

class StackTest(TestCase):
    def test_stack(self):
        stack = Stack()
        stack.push("i'am first element")
        stack.push("i'am second element")
        stack.push("i'am third element")
        self.assertEqual(stack.top.data, "i'am third element")
        self.assertEqual(stack.top.next_node.data, "i'am second element")
        self.assertEqual(stack.top.next_node.next_node.data, "i'am first element")
        try:
            hehe = stack.top.next_node.next_node.next_node.data
        except AttributeError:
            pass
        stack.push({"name": "foo", 5: "bar"})
        self.assertEqual(stack.top.data, {5: 'bar', 'name': 'foo'})

