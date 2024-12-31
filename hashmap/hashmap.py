from hashlib import sha256
from typing import TypeVar, Generic, Dict

T = TypeVar('T')


class HMnode(Generic[T]):
    "Hashmap Node"
    def __init__(self, key: str, val: T):
        self.key = key
        self.val = val
        self.next: HMnode[T] | None = None

class Hashmap(Generic[T]):
    "Hashmap Data Structure with a certain capacity."
    def __init__(self, capacity: int):
        self.__map: Dict[str, HMnode[T]] = {}
        self.__size = 0
        self.capacity = capacity

    def get_size(self):
        return self.__size
    
    def put(self, key: str, val: T)->bool:
        """if there's a capacity, it adds a new item to hashmap
        returns True if successfult, and False if it wasn't"""
        if(self.__size == self.capacity):
            return False
        
        hashedKey = self.__hash(key)

        try:
            hmNode = self.__map[hashedKey]
        except KeyError:
            self.__map[hashedKey] = HMnode[T](key, val)
            self.__size += 1
            return True
    
        newNode = HMnode[T](key, val)
        newNode.next = hmNode
        self.__map[hashedKey] = newNode
        self.__size += 1

        return True
        
    def __hash(self, key: str)->str:
        return sha256(key.encode()).hexdigest()

    def get(self, key: str)-> T | None:
        if(self.__size == 0):
            return None

        hashedKey = self.__hash(key)
        return self.__get_helper(key, hashedKey)

    def __get_helper(self, key: str, hashedKey)-> T | None:
        try:
            hmNode = self.__map[hashedKey]
        except KeyError:
            return None

        if(hmNode.key == key):
            return hmNode.val

        return self.__traverse(hmNode, key)

    def __traverse(self, node: HMnode[T] | None, key: str)-> T | None:
        if(node is None):
            return None
        
        if(node.key == key):
            return node.val
        
        return self.__traverse(node.next, key)

