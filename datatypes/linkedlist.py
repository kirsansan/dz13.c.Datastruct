from datatypes.node import Node


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def add_to_tail(self, object):
        """add a new object Node-type to the tail"""
        tmp_node = Node(object, None)
        if self.length == 0:
            self.head = tmp_node
        else:
            self.tail.next_node = tmp_node
        self.tail = tmp_node
        self.length += 1

    def add_to_head(self, object):
        """add a new object Node-type to the head"""
        tmp_node = Node(object, self.head)
        self.head = tmp_node
        self.length += 1

    def remove_from_head(self):
        """remove the data from the head of Queue
            hope __del__() for old Node will be called automatically
        """
        if self.length > 0:
            tmp_data = self.head.data
            self.head = self.head.next_node
            self.length -= 1
            return tmp_data

    def __len__(self):
        """just return the length (polymorphism does matter)"""
        return self.length

    def __str__(self):
        tmp_string = ""
        node = self.head
        if node is None:
            return None
        while node:
            tmp_string += f" {str(node.data)} ->"
            node = node.next_node
        tmp_string += ' None'
        return tmp_string

    def to_list(self):
        """
        :return: list with all node's data
        """
        tmp_list = []
        node = self.head
        if node is None:
            return None
        while node:
            tmp_list.append(node.data)
            node = node.next_node
        return tmp_list

    def get_data_by_id(self, search_id):
        """
        we are waiting for id which will be searched in every dictionary in our data
        non dictionary data will take exception, however we will intercept it
        :param search_id:
        :return: dictionary with field "id" == search_id
        """
        node = self.head
        while node:
            try:
                if node.data["id"] == search_id:
                    return node.data
                else:
                    print("I see some dict with id but this 'id' isn't interested for me")
            except TypeError:
                print("some shit in data")
            except KeyError:
                print("wrong key in dict data")
            if node.next_node:
                node = node.next_node
            else:
                return None
