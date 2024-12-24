from .priority_heap import PRIORITY_HEAP
from ..utils import errors

class TestPRIORITY_HEAP:

    def test_push(self):
        ph = PRIORITY_HEAP[str]()
        ph.push("eight", 8)
        ph.push("seven", 7)
        ph.push("nine", 9)

        assert ph.get_top() == "seven", errors.wrong_value(ph.get_top(), "seven")
        assert ph.get_size() == 3, "Size should be 3"

        ph.push("twenty", 20)
        ph.push("three", 3)
        ph.push("zero", 0)
        ph.push("ten", 10)

        assert ph.get_top() == "zero", errors.wrong_value(ph.get_top(), "zero")
        assert ph.get_size() == 7, "Size should be 7"


    def test_pop(self):
        ph = PRIORITY_HEAP[str]()
        ph.push("eight", 8)
        ph.push("seven", 7)
        ph.push("nine", 9)

        popped = ph.pop()
        assert popped.value == "seven", errors.wrong_value(popped.value, "seven")
        assert popped.priority == 7, errors.wrong_value(popped.priority, 7)

        assert ph.get_top() == "eight", errors.wrong_value(ph.get_top(), 'eight')
        assert ph.get_size() == 2, "Size should be 2"

        ph.push("twenty", 20)
        ph.push("three", 3)
        ph.push("zero", 0)
        ph.push("ten", 10)

        popped = ph.pop()
        assert popped.value == "zero", errors.wrong_value(popped.value, "zero")
        assert popped.priority == 0, errors.wrong_value(popped.priority, 0)

        assert ph.get_top() == "three", errors.wrong_value(ph.get_top(), 'three')
        assert ph.get_size() == 5, "Size should be 5"

    def test_delete(self):
        ph = PRIORITY_HEAP[str]()
        ph.push("eight", 8)
        ph.push("seven", 7)
        ph.push("nine", 9)

        assert ph.delete("seven") is True, "Should be True/Deleted"
        assert ph.get_top() == "eight", errors.wrong_value(ph.get_top(), "eight")

        assert ph.delete(5) is False, "Should be False"
        assert ph.delete(100) is False, "Should be False"
        assert ph.delete(-2) is False, "Should be False"
