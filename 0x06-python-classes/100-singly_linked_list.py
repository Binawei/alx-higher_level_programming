#!/usr/bin/python3
"""
This module Write a class Node that defines a node of a singly linked list 
"""
class Node:
    """A  class Node that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """
        Initailizes the class Node in any calling instance
        args:
            data: the data part of the node
            next_node: A pointer to the next node in the linked list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Returns the data of the linked list"""
        return self.__data


    @data.setter
    def data(self, value):
        """Sets the data of the linked list to value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value


    @property
    def next_node(self):
        """Retrieves or returns the pointer to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the value of the next pointer to value"""
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list """
    def __init__(self):
        """initializes with Private instance attribute: head"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in
        the list (increasing order)
        args:
            value: the new node to be sorted
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Defines the string representation of the Singlylinkedlist"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))



sll = SinglyLinkedList()

sll.sorted_insert(2)

sll.sorted_insert(5)

sll.sorted_insert(3)

sll.sorted_insert(10)

sll.sorted_insert(1)

sll.sorted_insert(-4)

sll.sorted_insert(-3)

sll.sorted_insert(4)

sll.sorted_insert(5)

sll.sorted_insert(12)

sll.sorted_insert(3)

print(sll)    
