from .singly import Singly 
from ..utils import errors
class TestSignly:

    def test_add_first(self):
        singlyList = Singly[int]()
        singlyList.add_first(1)
        singlyList.add_first(2)
        singlyList.add_first(3)

        assert singlyList.get_size() == 3, "Size should be 3"

        head = singlyList.get_head()
        assert head.data == 3, errors.wrong_value(head.data, 3)
        assert head.next.data == 2, errors.wrong_value(head.next.data , 2)
        assert head.next.next.data == 1, errors.wrong_value(head.next.next.data , 1)
        
    def test_add_last(self):
        singlyList = Singly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)

        assert singlyList.get_size() == 3, "Size should be 3"

        head = singlyList.get_head()
        assert head.data == 1, errors.wrong_value(head.data , 1)
        assert head.next.data == 2, errors.wrong_value(head.next.data , 2)
        assert head.next.next.data == 3, errors.wrong_value(head.next.next.data , 3)

    def test_delete_first(self):
        singlyList = Singly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)

        deleted1 = singlyList.delete_first()
        assert deleted1 == 1, errors.wrong_value(deleted1, 1)
        assert singlyList.get_size() == 2, "Size should be 2"
        
        deleted2 = singlyList.delete_first()
        assert deleted2 == 2, errors.wrong_value(deleted2, 2)
        assert singlyList.get_size() == 1, "Size should be 1"

        deleted3 = singlyList.delete_first()
        assert deleted3 == 3, errors.wrong_value(deleted3, 3)
        assert singlyList.get_size() == 0, "Size should be 0"

        deleted4 = singlyList.delete_first()
        assert deleted4 is None, "Should be None"

    def test_delete_last(self):
        singlyList = Singly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)

        deleted1 = singlyList.delete_last()
        assert deleted1 == 3, errors.wrong_value(deleted1, 3)
        assert singlyList.get_size() == 2, "Size should be 2"

        deleted2 = singlyList.delete_last()
        assert deleted2 == 2, errors.wrong_value(deleted2, 2)
        assert singlyList.get_size() == 1, "Size should be 1"

        deleted3 = singlyList.delete_last()
        assert deleted3 == 1, errors.wrong_value(deleted3, 1)
        assert singlyList.get_size() == 0, "Size should be 0"

    def test_delete_by_index(self):
        singlyList = Singly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)
        singlyList.add_last(4)
        singlyList.add_last(5)

        deleted1 = singlyList.delete_by_index(2)
        assert deleted1 == 3, errors.wrong_value(deleted1, 3)

        deleted2 = singlyList.delete_by_index(2)
        assert deleted2 == 4, errors.wrong_value(deleted2, 4)

        deleted3 = singlyList.delete_by_index(2)
        assert deleted3 == 5, errors.wrong_value(deleted3, 5)

        deleted4 = singlyList.delete_by_index(-1)
        assert deleted4 is None, "Should be None"

        deleted5 = singlyList.delete_by_index(10)
        assert deleted5 is None, "Should be None"
