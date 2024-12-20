from ..linkedlist.doubly import Doubly
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self):
        self.__list = Doubly[T]()
    
    def get_top(self)-> T | None:
        top = self.__list.get_head()
        if(top is None):
            return None
        return top.data
    
    def get_size(self)-> int:
        return self.__list.get_size()
    
    def push(self, val: T):
        return self.__list.add_first(val)

    def pop(self)-> T | None:
        return self.__list.delete_first()
