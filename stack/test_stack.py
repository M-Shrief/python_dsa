from .stack import Stack
from ..utils import errors

class TestStack:

    def test_push(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        assert stack.get_size() == 3, "Size should be 3"
        assert stack.get_top() == 3, errors.wrong_value(stack.get_top(), 3)

    def test_pop(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        stack.pop()
        assert stack.get_size() == 2, "Size should be 2"
        assert stack.get_top() == 2, errors.wrong_value(stack.get_top(), 2)

        stack.pop()
        assert stack.get_size() == 1, "Size should be 1"
        assert stack.get_top() == 1, errors.wrong_value(stack.get_top(), 1)

        stack.pop()
        assert stack.get_size() == 0, "Size should be 0"
        assert stack.get_top() is None, "Should be None"
