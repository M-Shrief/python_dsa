from typing import TypeVar, Generic

T = TypeVar('T')

class SinglyNode(Generic[T]):
    """Singly Node for a Singly Linkedlist"""
    def __init__(self, data: T, next=None):
        self.data = data
        self.next: SinglyNode[T] | None = next


class Singly(Generic[T]):
    """Singly linkedList"""
    def __init__(self):
        self.__size = 0
        self.__head: SinglyNode[T] | None = None
        self.__tail: SinglyNode[T] | None = None

    def get_size(self) -> int: 
        return self.__size
    
    def get_head(self) -> SinglyNode[T] | None: 
        return self.__head
    
    def get_tail(self) -> SinglyNode[T] | None: 
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
            return

        node = SinglyNode[T](val)
        # old singly.__tail.next will point to the new node
        self.__tail.next = node  # pyright:ignore[reportOptionalMemberAccess]
        # making the new node as singly.__tail
        self.__tail = node

        self.__size += 1

    def delete_first(self)-> T | None:
        if(self.__size == 0):
            return None

        current = self.__head

        if(self.__size == 1):
            self.__head = None
            self.__tail = None
        else:
            self.__head = current.next # pyright:ignore[reportOptionalMemberAccess]

        self.__size -= 1
        return current.data # pyright:ignore[reportOptionalMemberAccess]

    def delete_last(self)-> T | None:
        return self.delete_by_index(self.__size - 1)
    
    def delete_by_index(self, index: int)-> T | None:
        """Delete a node by its index, Note: index starts with Zero."""
        if (index < 0 or index >= self.__size):
            return None

        if(index == 0):
            return self.delete_first()
        
        current = self.__head
        for _ in range(index - 1):
            current = current.next # pyright:ignore[reportOptionalMemberAccess]
        
        removedNode = current.next # pyright:ignore[reportOptionalMemberAccess]
        current.next = current.next.next # pyright:ignore[reportOptionalMemberAccess]
        self.__size -= 1

        return removedNode.data # pyright:ignore[reportOptionalMemberAccess]

    def reverse(self):
        """Reverse the order of the linkedlist's nodes"""
        next: SinglyNode[T] | None = None
        prev: SinglyNode[T] | None = None
        
        current = self.__head
        while (current is not None):
            next = current.next
            current.next = prev

            prev = current
            current = next
        
        self.__head = prev

    def get_array(self)->list[T]:
        """Get all values from the linkedlist in an array"""
        arr: list[T] = []
        if(self.__size == 0):
            return arr
        
        current = self.__head
        arr.append(current.data)  # pyright:ignore[reportOptionalMemberAccess]
        while(current.next is not None):  # pyright:ignore[reportOptionalMemberAccess]
            current = current.next  # pyright:ignore[reportOptionalMemberAccess]
            arr.append(current.data)
        return arr