from unittest import TestCase
from datatypes.linkedlist import LinkedList

class LinkedListTest(TestCase):
    def test_llist_init_and_add(self):
        llist = LinkedList()
        llist.add_to_tail('llist1')
        llist.add_to_tail({"name": "somedata2", "value": "somevalue2"})
        llist.add_to_head('llist0')
        self.assertEqual(llist.to_list(), ['llist0', 'llist1', {'name': 'somedata2', 'value': 'somevalue2'}])

    def test_llist_length(self):
        llist = LinkedList()
        self.assertEqual(len(llist), 0)
        llist.add_to_tail('llist1')
        llist.add_to_tail({"name": "somedata2", "value": "somevalue2"})
        llist.add_to_head('llist0')
        self.assertEqual(len(llist), 3)

    def test_llist_get_by_id(self):
        llist = LinkedList()
        llist.add_to_tail('llist1')
        llist.add_to_tail({"name": "somedata2", "value": "somevalue2"})
        llist.add_to_head('llist0')
        llist.add_to_tail({"id": 5, "somedata5": "nothing"})
        llist.add_to_tail({"id": 2, "somedata2": "something"})
        self.assertEqual(llist.get_data_by_id(2),  {"id": 2, "somedata2": "something"})

