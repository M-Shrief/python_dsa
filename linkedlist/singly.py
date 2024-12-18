from typing import TypeVar, Generic

T = TypeVar('T')

class SinglyNode(Generic[T]):
# Singly linkedList Node
    def __init__(self, data: T, next=None):
        self.data = data
        if (next is not None):
            self.next = next


class Singly(Generic[T]):
# Singly linkedList
    def __init__(self):
        self.__size = 0
        self.__head: None | SinglyNode = None
        self.__tail: None | SinglyNode = None

    def get_size(self) -> int: 
        return self.__size
    
    def get_head(self) -> SinglyNode | None: 
        return self.__head
    
    def get_tail(self) -> SinglyNode | None: 
        return self.__tail

    def add_first(self, val: T):
        node = SinglyNode[T](val)
        if (self.__size == 0):
            self.__head = node
            self.__tail = node
        else:
            node.next = self.__head
            self.__head = node

        self.__size += 1
    
    def add_last(self, val: T):
        if(self.__size == 0):
            self.add_first(val)

        node = SinglyNode[T](val)
        # old singly.__tail.next will point to the new node
        self.__tail.next = node
        # making the new node as singly.__tail
        self.__tail = node

        self.__size += 1
    
