from ..linkedlist.doubly import Doubly, DoublyNode
from typing import TypeVar, Generic, Dict

T = TypeVar('T')

class Item(Generic[T]):
    """LRU's Item""" 
    def __init__(self, key: str, val: T):
        self.key = key
        self.val = val


class LRU(Generic[T]):
    """Least Recently Used caching data structure"""

    def __init__(self, capacity: int):
        # A Doubly Linked list
        self.__dl = Doubly[T]()
        # A hashmap using dictionaries, strings as a key
        # and the value is a DoublyNode which have Item[T] as data.
        self.__storage: Dict[str, DoublyNode[Item[T]]]  = {}
        # LRU capacity
        self.__capacity = capacity

    def get_size(self)->int:
        return self.__dl.get_size()

    def get_top(self)-> Item | None:
        top = self.__dl.get_head()
        if(top is None):
            return None
        return top.data

    def put(self, key: str, val: T):        
        if(self.get_size() == self.__capacity):
            self.__evict()

        newItem = Item[T](key,val)
        self.__dl.add_first(newItem)
        self.__storage[key] = self.__dl.get_head()
        return

    def __evict(self):
        if(self.get_size() == 0):
            return
        
        deleted = self.__dl.delete_last()
        del self.__storage[deleted.key]
        return
    
    def get(self, key: str)-> T | None:
        if(self.get_size() == 0):
            return None
        
        try:
            n = self.__storage[key]
        except KeyError:
            return None
        
        self.__dl.delete_by_node(n)
        self.__dl.add_first(n.data)
        self.__storage[key] = self.__dl.get_head()
        return n.data.val