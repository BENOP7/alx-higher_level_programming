#!/usr/bin/python3
'''
    Implements a singly linked list class and a node class
    representing each node in the linked list
'''


class Node:
    '''
        The node of a Singly linked list of integers
        - It has attribute data to store the integer
        - Has a next_node property that serves as pointer to the next node
    '''
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data
        if next_node is not None and not isinstance(next_node, self.__class__):
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node

    @property
    def data(self):
        '''
            returns the integer in the node of the linked list
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''
            sets the data property to a particular interger value
        '''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        '''
            returns the node that follows this node (self)
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''
            sets the node that follows this node (self) in the linked list
        '''
        if value is None or isinstance(value, self.__class__):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    '''
        A class that defines a singly linked list of integers
    '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''
            inserts a new node into the correct sorted position
        '''
        curr = self.__head
        i = 0

        if self.__head:
            while curr and value > curr.data:
                i += 1
                curr = curr.next_node
            curr = self.__head
            while i > 1:
                curr = curr.next_node
                i -= 1
            if i == 0:
                self.__head = Node(value, curr)
            else:
                curr.next_node = Node(value, curr.next_node)
        else:
            self.__head = Node(value)

    def __str__(self):
        '''
            prints the string representation of the linked list
        '''
        tmp = self.__head
        lst = []
        while tmp:
            lst.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(lst)
