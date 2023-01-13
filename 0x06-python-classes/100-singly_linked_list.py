#!/usr/bin/python3
"""
Node
Defines classes for a singly linked list implementation
with data and next node private instances in Node class
"""


class Node:
    """
    class Node definition

    Args:
        data (int): the data of the node
        next_node: the memory address of the next node
    """

    def __init__(self, data, next_node=None):
        """
        Initializes the Node instance

        Attributes
            data (int): the node data, of any type
            next_node: memory address of the next node,
                defaults to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter
        Return
                data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter

        Args:
            value (int): an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter
        Return:
            next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter

        Args:
            value : address of the next node, can be None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Singly Linked List presentation """

    def __init__(self):
        """ instantiate the Singly Linked List class """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a node into and sorts the SinglyLinkedList

        the node is inserted at the correct ordered numerical position

        Args:
            value (node): the new node to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

    def __str__(self):
        """
        Represents the print() of the entire singly linked list
        """
        printable = []

        if self.__head is not None:
            temp = self.__head
            while temp:
                printable.append(str(temp.data))
                temp = temp.next_node
        return ('\n'.join(printable))
