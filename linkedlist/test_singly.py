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

