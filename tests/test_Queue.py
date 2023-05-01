from unittest import TestCase

from datatypes.node import Node
from datatypes.queue import Queue

class QueueTest(TestCase):
    def test_stack_init_and_push(self):
        queue = Queue()
        queue.add("i'am first element")
        queue.add(2)
        queue.add("i'am third element")
        self.assertEqual(queue.head.data, "i'am first element")
        self.assertEqual(queue.head.next_node.data, 2)
        self.assertEqual(queue.head.next_node.next_node.data, "i'am third element")
        try:
            temp_value = queue.head.next_node.next_node.next_node.data
        except AttributeError:
            pass
        queue.add({"name": "foo", 5: "bar"})
        self.assertEqual(queue.tail.data, {5: 'bar', 'name': 'foo'})

    def test_stack_pop(self):
        queue = Queue()
        queue.add("i'am first element")
        queue.add(2)
        queue.add("i'am third element")
        self.assertEqual(queue.remove(), "i'am first element")
        self.assertEqual(queue.remove(), 2)
        self.assertEqual(queue.remove(), "i'am third element")
        self.assertEqual(queue.remove(), None)

    def test_length(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)
        queue.add("i'am first element")
        queue.add(2)
        queue.add("i'am third element")
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.remove(), "i'am first element")
        self.assertEqual(queue.remove(), 2)
        self.assertEqual(queue.remove(), "i'am third element")
        self.assertEqual(queue.remove(), None)
        self.assertEqual(len(queue), 0)
