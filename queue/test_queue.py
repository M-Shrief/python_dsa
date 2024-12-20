from .queue import Queue
from ..utils import errors

class TestQueue:

    def test_enqueu(self):
        queue = Queue[int]()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert queue.get_size() == 3, "Size should be 3"
        assert queue.get_first() == 1, errors.wrong_value(queue.get_first(), 1)

    def test_dequeu(self):
        queue = Queue[int]()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.dequeue()
        assert queue.get_size() == 2, "Size should be 2"
        assert queue.get_first() == 2, errors.wrong_value(queue.get_first(), 2)

        queue.dequeue()
        assert queue.get_size() == 1, "Size should be 1"
        assert queue.get_first() == 3, errors.wrong_value(queue.get_first(), 3)

        queue.dequeue()
        assert queue.get_size() == 0, "Size should be 0"
        assert queue.get_first() is None, "Should be None"
