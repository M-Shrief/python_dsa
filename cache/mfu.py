from ..heap.heap import Heap
from typing import TypeVar, Generic, Dict

T = TypeVar('T')

class MFUNode(Generic[T]):
    """Most Frequenty Used node"""
    def __init__(self, key: str, val: T):
        self.key = key
        self.val = val
        self.freq = 0

class MFU(Generic[T]):
    """Most Frequenty Used cache data structure"""

    def __init__(self, capacity: int):
        self.__max_heap = Heap[MFUNode[T]](self.__is_most_frequent)
        self.__storage: Dict[str, MFUNode[T]] = {}
        self.__capacity = capacity
        self.__size = 0

    def get_size(self):
        return self.__size
    
    def get_top(self)->T:
        return self.__max_heap.get_top().val
    
    def put(self, key: str, val: T):
        newNode = MFUNode[T](key,val)

        if(self.__size == self.__capacity):
            self.__evict()
        
        self.__max_heap.push(newNode)
        self.__storage[key] = newNode
        self.__size += 1

    def __evict(self):
        if(self.__size == 0):
            return
        
        node = self.__max_heap.get_top()
        self.__max_heap.pop()
        del self.__storage[node.key]

        self.__size -= 1

    def get(self, key: str)-> T | None:
        if(self.__size == 0):
            return None
        
        try:
            n = self.__storage[key]
        except KeyError:
            return None

        self.__max_heap.delete(n)
        n.freq += 1
        self.__max_heap.push(n)
        return n.val

    

    def __is_most_frequent(self, a: MFUNode[T], b: MFUNode[T])-> bool:
        return a.freq > b.freq