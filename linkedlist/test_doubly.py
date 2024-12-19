from .doubly import Doubly
from ..utils import errors

class TestDoubly:

    def test_add_first(self):
        doublyList = Doubly[int]()
        doublyList.add_first(1)
        doublyList.add_first(2)
        doublyList.add_first(3)

        assert doublyList.get_size() == 3, "Size should be 3"

        head = doublyList.get_head()
        assert head.data == 3, errors.wrong_value(head.data, 3)
        assert head.next.data == 2, errors.wrong_value(head.next.data, 2)
        assert head.next.next.data == 1, errors.wrong_value(head.next.next.data, 1)

        assert head.prev is None, errors.wrong_value(head.prev, None)

        assert head.next.prev == head, errors.wrong_value(head.next.prev, head)
        assert head.next.prev.data == 3, errors.wrong_value(head.next.prev.data, 3)

        assert head.next.next.prev == head.next, errors.wrong_value(head.next.next.prev, head.next)
        assert head.next.next.prev.data == 2, errors.wrong_value(head.next.next.prev.data, 2)

    def test_add_last(self):
        doublyList = Doubly[int]()
        doublyList.add_last(1)
        doublyList.add_last(2)
        doublyList.add_last(3)

        assert doublyList.get_size() == 3, "Size should be 3"

        head = doublyList.get_head()
        assert head.data == 1, errors.wrong_value(head.data, 1)
        assert head.next.data == 2, errors.wrong_value(head.next.data, 2)
        assert head.next.next.data == 3, errors.wrong_value(head.next.next.data, 3)

        assert head.prev is None, errors.wrong_value(head.prev, None)

        assert head.next.prev == head, errors.wrong_value(head.next.prev, head)
        assert head.next.prev.data == 1, errors.wrong_value(head.next.prev.data, 1)

        assert head.next.next.prev == head.next, errors.wrong_value(head.next.next.prev, head.next)
        assert head.next.next.prev.data == 2, errors.wrong_value(head.next.next.prev.data, 2)

    def test_delete_first(self):
        doublyList = Doubly[int]()
        doublyList.add_first(1)
        doublyList.add_first(2)
        doublyList.add_first(3)

        deleted1 = doublyList.delete_first()
        assert deleted1 == 3, errors.wrong_value(deleted1, 3)
        assert doublyList.get_size() == 2, "Size should be 2"

        deleted2 = doublyList.delete_first()
        assert deleted2 == 2, errors.wrong_value(deleted2, 2)
        assert doublyList.get_size() == 1, "Size should be 1"

        deleted3 = doublyList.delete_first()
        assert deleted3 == 1, errors.wrong_value(deleted3, 1)
        assert doublyList.get_size() == 0, "Size should be 0"

    def test_delete_last(self):
        doublyList = Doubly[int]()
        doublyList.add_first(1)
        doublyList.add_first(2)
        doublyList.add_first(3)

        deleted1 = doublyList.delete_last()
        assert deleted1 == 1, errors.wrong_value(deleted1, 1)
        assert doublyList.get_size() == 2, "Size should be 2"

        deleted2 = doublyList.delete_last()
        assert deleted2 == 2, errors.wrong_value(deleted2, 2)
        assert doublyList.get_size() == 1, "Size should be 1"

        deleted3 = doublyList.delete_last()
        assert deleted3 == 3, errors.wrong_value(deleted3, 3)
        assert doublyList.get_size() == 0, "Size should be 0"

