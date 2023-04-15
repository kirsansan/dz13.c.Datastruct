from unittest import TestCase

from datatypes.node import Node
from datatypes.stack import Stack

class NodeTest(TestCase):
    def test_node(self):
        node1 = Node(5, None)
        self.assertEqual(str(node1), "Node(object=5, next_node=None)")
        self.assertEqual(node1.__repr__(), "Node(object=5, next_node=None)")
        node2 = Node("yahoo", node1)
        self.assertEqual(str(node2), "Node(object=yahoo, next_node=Node(object=5, next_node=None))")

        # self.assertTrue("1", "1")


