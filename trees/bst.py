from ..queue.queue import Queue
from typing import TypeVar, Generic, List, Literal, Callable

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

    def delete(self, val: T) -> bool:
        """Delete certain value from BST.
        if it's deleted successfully, it returns True, if it doesn't exists it return False"""
        if(self.__size == 0):
            return False
        
        if(self.__size == 1):
            if(self.__root.val == val):
                self.__root = None
                self.__size -= 1
                return True
            else:
                return False
            
        result = self.__delete_node(self.__root, val)
        # Return the boolean value only
        isDeleted = result[1]
        if(isDeleted):
            self.__size -= 1
        return isDeleted

    def __delete_node(self, node: BSNode[T], val: T) -> tuple[BSNode[T] | None, bool]:
        if(node is None):
            return None, False 

        if(val < node.val):
            return self.__delete_node(node.left, val)
        if(val > node.val):
            return self.__delete_node(node.right, val)

        ifLeftNodeExists = node.left is not None       
        ifRightNodeExists = node.right is not None       
        
        # if it have 2 childs:
        # set node.val to the maximum child in the left subtree.
        # then go back and delete that leaf key.
        if(ifLeftNodeExists and ifRightNodeExists):
            maximumValueInLeftSubTree = self.__get_maximum_node(node.left).val
            result = self.__delete_node(node.left, maximumValueInLeftSubTree)
            node.left = result[0]
            node.val = maximumValueInLeftSubTree
            return node, True
        
        # Note: from here on, don't return the node value to 
        # avoid deleting other nodes becuase of recursive calls.
        parent = self.get_parent(node.val)
        if(ifLeftNodeExists):
            if(parent is not None):
                if(parent.val >= node.val):
                    parent.left = node.left
                else:
                    parent.right = node.left
            # If parent is None
            else:
                self.__root = node.left

            return None, True

        elif(ifRightNodeExists):
            if(parent is not None):
                if(parent.val >= node.val):
                    parent.left = node.right
                else:
                    parent.right = node.right
            # If parent is None
            else:
                self.__root = node.right

            return None, True
        
        else:
            if(node.val <= parent.val):
                parent.left = None
                return None, True
            else:
                parent.right = None
                return None, True

    def BFT(self)->List[T]:
        arr: List[T] = []
        if(self.__size == 0):
            return arr
        
        queue = Queue[BSNode[T]]()
        queue.enqueue(self.__root)

        while(queue.get_size() > 0):
            current = queue.dequeue()
            arr.append(current.val)

            leftChild = current.left
            if(leftChild is not None):
                queue.enqueue(leftChild)
            
            rightChild = current.right
            if(rightChild is not None):
                queue.enqueue(rightChild)
        
        return arr


    def BFS(self, val: T)->BSNode[T] | None:
        if(self.__size == 0):
            return None
        node: BSNode[T] | None = None

        queue = Queue[BSNode[T]]()
        queue.enqueue(self.__root)

        while(queue.get_size() > 0):
            current = queue.dequeue()
            if(val == current.val):
                node = current
                break

            leftChild = current.left
            if(leftChild is not None):
                queue.enqueue(leftChild)
            
            rightChild = current.right
            if(rightChild is not None):
                queue.enqueue(rightChild)
        
        return node

    def DFT(self, method: Literal['preOrder', 'inOrder', 'postOrder'])->List[T]:
        arr: List[T] = []
        if(self.__size == 0):
            return arr
        
        match method:
            case "preOrder":
                return self.__pre_order_traversal(self.__root, arr)
            case "inOrder":
                return self.__in_order_traversal(self.__root, arr)
            case "postOrder":
                return self.__post_order_traversal(self.__root, arr)
            case _: # default
                return self.__in_order_traversal(self.__root, arr)

        return arr
    def __pre_order_traversal(self, node: BSNode[T] | None, arr: List[T]):
        if(node is None):
            return arr

        arr.append(node.val)
        self.__pre_order_traversal(node.left, arr)
        self.__pre_order_traversal(node.right, arr)
        return arr

    def __in_order_traversal(self, node: BSNode[T] | None, arr: List[T]):
        if(node is None):
            return arr

        self.__in_order_traversal(node.left, arr)
        arr.append(node.val)
        self.__in_order_traversal(node.right, arr)
        return arr
    
    def __post_order_traversal(self, node: BSNode[T] | None, arr: List[T]):
        if(node is None):
            return arr

        self.__post_order_traversal(node.left, arr)
        self.__post_order_traversal(node.right, arr)
        arr.append(node.val)
        return arr
    
            
