from ..linkedlist.singly import Singly
from typing import TypeVar, Generic

T = TypeVar('T')

class Queue(Generic[T]):
    """A Queue using a Linkedlist."""

    def __init__(self):
        self.__list = Singly[T]()
    
    def get_first(self)-> T | None:
        first = self.__list.get_head()
        if(first is None):
            return None
        return first.data
    
    def get_size(self)-> int:
        return self.__list.get_size()
    
    def enqueue(self, val: T):
        self.__list.add_last(val)
    
    def dequeue(self)-> T | None:
        return self.__list.delete_first()