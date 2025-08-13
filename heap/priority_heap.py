from typing import TypeVar, Generic
T = TypeVar('T')

class PH_Node(Generic[T]):
    """Node for Priority Heap Data Structure"""
    def __init__(self, value: T, priority: int):
        self.value = value
        self.priority = priority



class PRIORITY_HEAP(Generic[T]):
    """Priority Heap, every Node/item takes a value and its priority
    The smaller the priority, the more it's prioritized"""
    def __init__(self):
        self.__list: list[PH_Node[T]] = []

    def __is_preceding(self, a: PH_Node[T], b: PH_Node[T])-> bool:
        """Comparing the priority value for 2 node in the priority heap
        The smaller the value, the more it's prioritized"""
        return a.priority < b.priority

    def get_top(self)-> T:
        return self.__list[0].value

    def get_size(self)->int:
        return len(self.__list)


    def push(self, val: T, priority: int):
        newNode = PH_Node[T](val, priority)
        self.__list.append(newNode)
        self.__heapify_up(len(self.__list) - 1)
    
    def pop(self)-> PH_Node[T] | None:
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
            if(self.__list[i].value == val):
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
        
        isPreceding = self.__is_preceding(self.__list[child], self.__list[parent])
        if(isPreceding is False):
            return
        
        self.__swap(child, parent)
        self.__heapify_up(parent)

    def __heapify_down(self, parent: int):
        """Applying Heap constraints going down"""
        current = parent
        leftChild = parent * 2 + 1
        rightChild = parent * 2 + 2

        if(leftChild < len(self.__list) and self.__is_preceding(self.__list[leftChild], self.__list[current])):
            current = leftChild
        
        if(leftChild < len(self.__list) and self.__is_preceding(self.__list[leftChild], self.__list[current])):
            current = rightChild

        if(current == parent):
            return

        self.__swap(current, parent)
        self.__heapify_down(current)

    def __swap(self, id1: int, id2: int):
        self.__list[id1], self.__list[id2] = self.__list[id2], self.__list[id1]
