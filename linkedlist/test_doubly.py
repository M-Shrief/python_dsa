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

    def test_delete_by_index(self):
        doublyList = Doubly[int]()
        doublyList.add_last(1)
        doublyList.add_last(2)
        doublyList.add_last(3)
        doublyList.add_last(4)
        doublyList.add_last(5)

        deleted1 = doublyList.delete_by_index(2)
        assert deleted1 == 3, errors.wrong_value(deleted1, 3)
        assert doublyList.get_size() == 4, "Size should be 4"

        deleted2 = doublyList.delete_by_index(2)
        assert deleted2 == 4, errors.wrong_value(deleted2, 4)
        assert doublyList.get_size() == 3, "Size should be 3"

        deleted3 = doublyList.delete_by_index(2)
        assert deleted3 == 5, errors.wrong_value(deleted3, 5)
        assert doublyList.get_size() == 2, "Size should be 2"

        deleted4 = doublyList.delete_by_index(2)
        assert deleted4 is None

        deleted4 = doublyList.delete_by_index(-1)
        assert deleted4 is None

        deleted4 = doublyList.delete_by_index(20)
        assert deleted4 is None

    def test_delete_by_node(self):
        doublyList = Doubly[int]()
        doublyList.add_last(1)
        doublyList.add_last(2)
        doublyList.add_last(3)
        doublyList.add_last(4)
        doublyList.add_last(5)

        head = doublyList.get_head()
        two = head.next
        deleted1 = doublyList.delete_by_node(two)
        assert deleted1 == 2, errors.wrong_value(deleted1, 2)
        assert doublyList.get_size() == 4, "Size should be 4"
        assert head.next.data == 3, errors.wrong_value(head.next.data, 3)

        tail = doublyList.get_tail()
        four = tail.prev
        deleted2 = doublyList.delete_by_node(four)
        assert deleted2 == 4, errors.wrong_value(deleted2, 4)
        assert doublyList.get_size() == 3, "Size should be 3"
        assert tail.prev.data == 3, errors.wrong_value(head.next.data, 3)

    def test_reverse(self):
        singlyList = Doubly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)
        singlyList.add_last(4)
        singlyList.add_last(5)

        singlyList.reverse()

        head = singlyList.get_head()
        assert head.data == 5, errors.wrong_value(head.data, 5)
        assert head.next.data == 4, errors.wrong_value(head.next.data, 4)
        assert head.next.next.data == 3, errors.wrong_value(head.next.next.data, 3)
        assert head.next.next.next.data == 2, errors.wrong_value(head.next.next.next.data, 2)
        assert head.next.next.next.next.data == 1, errors.wrong_value(head.next.next.next.next.data, 1)

    def test_get_array(self):
        singlyList = Doubly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)
        singlyList.add_last(4)
        singlyList.add_last(5)

        arr1 = singlyList.get_array()
        assert arr1 == [1,2,3,4,5]
        assert arr1 != [1,2,4,5,3]

        singlyList.reverse()
        arr2 = singlyList.get_array()
        assert arr2 == [5,4,3,2,1]
        assert arr2 != [5,4,1,3,2]