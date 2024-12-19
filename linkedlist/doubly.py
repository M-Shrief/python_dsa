from typing import TypeVar, Generic

T = TypeVar('T')

class DoublyNode(Generic[T]):
    """Doubly Node for a Doubly Linkedlist"""
    def __init__(self, data: T, prev=None, next=None):
        self.data = data
        self.prev: DoublyNode | None = prev
        self.next: DoublyNode | None = next

class Doubly(Generic[T]):

    def __init__(self):
        self.__size: int = 0
        self.__head: DoublyNode | None = None
        self.__tail: DoublyNode | None = None
    
    def get_size(self)->int:
        return self.__size
    
    def get_head(self)->DoublyNode | None:
        return self.__head
    
    def get_tail(self)->DoublyNode | None:
        if(self.__size <= 1):
            return self.__head
        return self.__tail
    
    def add_first(self, val: T):
        doublyNode = DoublyNode[T](val)

        if(self.__size == 0):
            self.__head = doublyNode
        else:
            self.__head.prev = doublyNode
            doublyNode.next = self.__head
            self.__head = doublyNode
            if(self.__size == 1):
                self.__tail = doublyNode.next
        
        self.__size += 1

    def add_last(self, val: T):
        if(self.__size == 0):
            return self.add_first(val)
        
        doublyNode = DoublyNode[T](val)
        self.get_tail().next = doublyNode
        doublyNode.prev = self.get_tail()
        self.__tail = doublyNode

        self.__size += 1

    def delete_first(self)-> T | None:
        if(self.__size == 0):
            return None
        
        node = self.__head
        if(self.__size == 1):
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return node.data
        
        self.__head = node.next
        self.__head.prev = None
        self.__size -= 1
        return node.data

    def delete_last(self)-> T | None:
        if(self.__size == 0 ):
            return None
        if(self.__size == 1):
            return self.delete_first()

        node = self.get_tail()
        self.__tail = node.prev
        self.__tail.next = None
        
        self.__size -= 1
        return node.data

    def delete_by_index(self, index: int)-> T | None:
        if(index < 0 or index >= self.__size):
            return None
        if(index == 0):
            return self.delete_first()
        if(index == self.__size - 1):
            return self.delete_last()
        
        current = self.__head
        for count in range(index - 1):
            current = current.next

        removedNode = current.next
        current.next = removedNode.next
        current.next.prev = current

        self.__size -= 1
        return removedNode.data

    def delete_by_node(self, node: DoublyNode)-> T | None:
        if(node == self.__head):
            return self.delete_first()
        if(node == self.__tail):
            return self.delete_last()
        
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        
        self.__size -= 1
        return node.data

    def reverse(self):
        """Reverse the order of the linkedlist's nodes"""
        prev: DoublyNode | None = None
        next: DoublyNode | None = None
        current = self.__head

        while(current is not None):
            next = current.next
            current.next = prev
            current.prev = next

            prev = current
            current = next
        
        self.__head = prev

    def get_array(self)->list[T]:
        """Get all values from the linkedlist in an array"""
        arr: list[T] = []
        if(self.__size == 0):
            return arr
        
        current = self.__head
        arr.append(current.data)
        while(current.next is not None):
            current = current.next
            arr.append(current.data)
        return arr