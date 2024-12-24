from .heap import Heap
from ..utils import errors

class TestHeap:

    """Min Heap tests"""
    def __is_smaller(self, a: int, b: int)->bool:
        return a < b

    def test_push_min_heap(self):
        h = Heap[int](self.__is_smaller)  
        h.push(1)
        h.push(6)
        h.push(4)

        assert h.get_top() == 1, errors.wrong_value(h.get_top(), 1)
        assert h.get_size() == 3, "Size should be 3"

        h.push(-3)
        h.push(-1)
        h.push(-5)

        assert h.get_top() == -5, errors.wrong_value(h.get_top(), -5)
        assert h.get_size() == 6, "Size should be 6"

    def test_pop_min_heap(self):
        h = Heap[int](self.__is_smaller)  
        h.push(1)
        h.push(6)
        h.push(4)

        popped = h.pop()
        assert  popped == 1, errors.wrong_value(popped, 1)
        assert h.get_top() == 4, errors.wrong_value(h.get_top(), 1)
        assert h.get_size() == 2, "Size should be 2"

        h.push(-3)
        h.push(-1)
        h.push(-5)

        popped = h.pop()
        assert  popped == -5, errors.wrong_value(popped, -5)
        assert h.get_top() == -3, errors.wrong_value(h.get_top(), -3)
        assert h.get_size() == 4, "Size should be 4"

    def test_delete_min_heap(self):
        h = Heap[int](self.__is_smaller)  
        h.push(1)
        h.push(6)
        h.push(4)

        assert h.delete(1) is True, "Should be True/Deleted"
        assert h.get_top() == 4, errors.wrong_value(h.get_top(), 4)

        assert h.delete(5) is False, "Should be False"
        assert h.delete(100) is False, "Should be False"
        assert h.delete(-2) is False, "Should be False"

    """Max Heap tests"""
    def __is_bigger(self, a: int, b: int)->bool:
        return a > b

    def test_push_max_heap(self):
        h = Heap[int](self.__is_bigger)  
        h.push(1)
        h.push(6)
        h.push(4)

        assert h.get_top() == 6, errors.wrong_value(h.get_top(), 6)
        assert h.get_size() == 3, "Size should be 3"

        h.push(-3)
        h.push(100)
        h.push(-100)

        assert h.get_top() == 100, errors.wrong_value(h.get_top(), 100)
        assert h.get_size() == 6, "Size should be 6"

    def test_pop_max_heap(self):
        h = Heap[int](self.__is_bigger)  
        h.push(1)
        h.push(6)
        h.push(4)

        popped = h.pop()
        assert  popped == 6, errors.wrong_value(popped, 6)
        assert h.get_top() == 4, errors.wrong_value(h.get_top(), 1)
        assert h.get_size() == 2, "Size should be 2"

        h.push(-3)
        h.push(-1)
        h.push(-5)

        popped = h.pop()
        assert  popped == 4, errors.wrong_value(popped, 4)
        assert h.get_top() == 1, errors.wrong_value(h.get_top(), 1)
        assert h.get_size() == 4, "Size should be 4"

    def test_delete_max_heap(self):
        h = Heap[int](self.__is_bigger)  
        h.push(1)
        h.push(6)
        h.push(4)

        assert h.delete(1) is True, "Should be True/Deleted"
        assert h.get_top() == 6, errors.wrong_value(h.get_top(), 6)

        assert h.delete(5) is False, "Should be False"
        assert h.delete(100) is False, "Should be False"
        assert h.delete(-2) is False, "Should be False"
