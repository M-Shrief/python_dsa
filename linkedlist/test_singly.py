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
        assert head.data == 3, errors.wrong_value(head.data, 3) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.data == 2, errors.wrong_value(head.next.data , 2) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.next.data == 1, errors.wrong_value(head.next.next.data , 1) # pyright:ignore[reportOptionalMemberAccess]
        
    def test_add_last(self):
        singlyList = Singly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)

        assert singlyList.get_size() == 3, "Size should be 3"

        head = singlyList.get_head()
        assert head.data == 1, errors.wrong_value(head.data , 1) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.data == 2, errors.wrong_value(head.next.data , 2) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.next.data == 3, errors.wrong_value(head.next.next.data , 3) # pyright:ignore[reportOptionalMemberAccess]

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

    def test_reverse(self):
        singlyList = Singly[int]()
        singlyList.add_last(1)
        singlyList.add_last(2)
        singlyList.add_last(3)
        singlyList.add_last(4)
        singlyList.add_last(5)

        singlyList.reverse()

        head = singlyList.get_head()
        assert head.data == 5, errors.wrong_value(head.data, 5) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.data == 4, errors.wrong_value(head.next.data, 4) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.next.data == 3, errors.wrong_value(head.next.next.data, 3) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.next.next.data == 2, errors.wrong_value(head.next.next.next.data, 2) # pyright:ignore[reportOptionalMemberAccess]
        assert head.next.next.next.next.data == 1, errors.wrong_value(head.next.next.next.next.data, 1) # pyright:ignore[reportOptionalMemberAccess]

    def test_get_array(self):
        singlyList = Singly[int]()
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