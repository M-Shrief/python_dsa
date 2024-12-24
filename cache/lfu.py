from ..heap.heap import Heap
from typing import TypeVar, Generic, Dict

T = TypeVar('T')

class LFUNode(Generic[T]):
    def __init__(self, key: str, val: T, freq: int):
        self.key = key
        self.val = val
        self.freq = freq

class LFU(Generic[T]):
    """Least Frequenty Used cache data structure"""
    def __init__(self, capacity: int):
        self.__min_heap = Heap[LFUNode[T]](self.__is_least_frequent)
        self.__storage: Dict[str, LFUNode[T]]  = {}
        self.__size = 0
        self.__capacity = capacity

    def get_size(self)->int:
        return self.__size
    
    def get_top(self)-> T: 
        return self.__min_heap.get_top().val

    def get(self, key: str)-> T | None:
        if(self.__size == 0):
            return None
        
        try:
            n = self.__storage[key]
        except KeyError:
            return None
        
        self.__min_heap.delete(n)
        n.freq += 1
        self.__min_heap.push(n)
        return n.val


    def put(self, key: str, val: T):
        newNode = LFUNode[T](key, val, 0)

        if(self.__size == self.__capacity):
            self.__evict()

        self.__min_heap.push(newNode)
        self.__storage[key] = newNode
        self.__size += 1

    def __evict(self):
        if(self.__size == 0):
            return
        
        node = self.__min_heap.get_top()
        self.__min_heap.pop()
        del self.__storage[node.key]

        self.__size -= 1

    def __is_least_frequent(self, a: LFUNode[T], b: LFUNode[T])-> bool:
        return a.freq < b.freq