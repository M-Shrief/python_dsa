from typing import TypeVar, Generic

T = TypeVar("T")

class BSNode(Generic[T]):
    """Binary Search Tree node"""
    def __init__(self, val: T):
        self.val = val
        self.left: BSNode | None = None
        self.right: BSNode | None = None

class BST(Generic[T]):
    """Binary Search Tree"""
    def __init__(self):
        self.__root: BSNode | None = None
        self.__size: int = 0
    
    def get_size(self)->int:
        return self.__size
    
    def get_root(self)-> BSNode[T] | None:
        return self.__root
    
    def insert(self, val: T):
        if(self.__size == 0):
            newNode = BSNode[T](val)
            self.__root = newNode
            self.__size += 1
        else:
            self.__insert_node(self.__root, val)
    
    def __insert_node(self, node: BSNode, val: T):
        if(val <= node.val):
            if(node.left is not None):
                self.__insert_node(node.left, val)
            else:
                newNode = BSNode[T](val)
                node.left = newNode
                self.__size += 1
        else:
            if(node.right is not None):
                self.__insert_node(node.right, val)
            else:
                newNode = BSNode[T](val)
                node.right = newNode
                self.__size += 1

    def search(self, val: T)-> BSNode[T] | None:
        if(self.__size == 0):
            return None
        return self.__search_node(self.__root, val)

    def __search_node(self, node: BSNode[T] | None, val: T)-> BSNode[T] | None:
        if(node is None):
            return None
        
        if(val == node.val):
            return node

        if(val < node.val):
            return self.__search_node(node.left, val)
        else:
            return self.__search_node(node.right, val)
 
    def get_parent(self, val: T) -> BSNode[T] | None:
        """Get the parent node, which one of its childs have val as value"""
        if(self.__size == 0):
            return None
        return self.__get_parent_node(self.__root, val)

    def __get_parent_node(self, node: BSNode[T], val: T) -> BSNode[T] | None:
        if(node is None or node.val == val):
            return None
        
        if(val < node.val):
            if(val == node.left.val):
                return node
            return self.__get_parent_node(node.left, val)
        else:
            if(val == node.right.val):
                return node
            return self.__get_parent_node(node.right, val)

    def get_maximum(self) -> T | None:
        if(self.__size == 0):
            return None
        maximum =  self.__get_maximum_node(self.__root)
        return maximum.val

    def __get_maximum_node(self, node: BSNode[T]) -> BSNode[T] | None:
        if(node is None):
            return None
        if(node.right is None):
            return node
        else:
            return self.__get_maximum_node(node.right)

    def get_minimum(self) -> T | None:
        if(self.__size == 0):
            return None
        minimum =  self.__get_minimum_node(self.__root)
        return minimum.val

    def __get_minimum_node(self, node: BSNode[T]) -> BSNode[T] | None:
        if(node is None):
            return None
        if(node.left is None):
            return node
        else:
            return self.__get_minimum_node(node.left)