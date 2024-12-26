from ..linkedlist.doubly import Doubly, DoublyNode
from typing import TypeVar, Generic, Dict

T = TypeVar('T')

class Item(Generic[T]):
    def __init__(self, key: str, val: T):
        self.key = key
        self.val = val


class MRU(Generic[T]):
    """Most Recently Used cache data structure"""
    global Item

    def __init__(self, capacity: int):
        self.__doubly = Doubly[Item[T]]()
        self.__storage: Dict[str, DoublyNode[Item[T]]] = {}
        self.__capacity = capacity

    def get_size(self) -> int:
        return self.__doubly.get_size()
    
    def get_top(self) -> Item[T]:
        top = self.__doubly.get_head()
        if(top is None):
            return None
        return top.data
    
    def put(self, key: str, val: T):
        if(self.get_size() == self.__capacity):
            self.__evict()

        newItem = Item[T](key, val)
        self.__doubly.add_first(newItem)
        self.__storage[key] = self.__doubly.get_head()
        return

    def __evict(self):
        if(self.get_size() == 0):
            return

        deleted = self.__doubly.delete_last()
        del self.__storage[deleted.key]
        return

    def get(self, key: str) -> T | None:
        if(self.get_size() == 0):
            return None
        
        try:
            n = self.__storage[key]
        except KeyError:
            return None
        
        self.__doubly.delete_by_node(n)
        self.__doubly.add_last(n.data)
        self.__storage[key] = self.__doubly.get_tail()

        return n.data.val
