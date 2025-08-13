from typing import TypeVar, Generic, Callable

T = TypeVar('T')

class Heap(Generic[T]):
    """Heap Data Structure.
    Takesfunction as an argument to compare items from the same type"""
    def __init__(self, compareFn: Callable[[T, T], bool]):
        self.__list: list[T] = []
        self.__compare: Callable[[T, T], bool] = compareFn

    def __swap(self, id1: int, id2: int):
        self.__list[id1], self.__list[id2] = self.__list[id2], self.__list[id1]

    def get_top(self)-> T:
        return self.__list[0]

    def get_size(self)->int:
        return len(self.__list)

    def push(self, val: T):
        self.__list.append(val)
        self.__heapify_up(len(self.__list) - 1)
    
    def pop(self)-> T | None:
        if(len(self.__list) == 0):
            return None
        
        top = self.__list[0]

        self.__swap(0, len(self.__list) - 1)
        self.__list = self.__list[0:len(self.__list) - 1]
        self.__heapify_down(0)

        return top

    def delete(self, val: T)-> bool:
        i = 0
        found = False
        while(i < len(self.__list)):
            if(self.__list[i] == val):
                found = True
                break
            i += 1

        if(found is True):
            self.__swap(i, len(self.__list) - 1)
            self.__list = self.__list[0: len(self.__list) - 1]
            self.__heapify_down(i)
            return True
        
        return False        
    
    def __heapify_up(self, child: int):
        """Applying Heap constraints going up"""
        if(child <= 0):
            return 
        parent = child - 1 >> 1
        
        comparison = self.__compare(self.__list[child], self.__list[parent])
        if(comparison is False):
            return
        
        self.__swap(child, parent)
        self.__heapify_up(parent)

    def __heapify_down(self, parent: int):
        """Applying Heap constraints going down"""
        current = parent
        leftChild = parent * 2 + 1
        rightChild = parent * 2 + 2

        if(leftChild < len(self.__list) and self.__compare(self.__list[leftChild], self.__list[current])):
            current = leftChild
        
        if(leftChild < len(self.__list) and self.__compare(self.__list[leftChild], self.__list[current])):
            current = rightChild

        if(current == parent):
            return

        self.__swap(current, parent)
        self.__heapify_down(current)
 