from singly import Singly 

def test_singly():
    singlyList = Singly[int]()
    singlyList.add_last(1)
    singlyList.add_last(2)
    singlyList.add_last(3)

    assert singlyList.get_size() == 3, "Size should be 3"

    head = singlyList.get_head()
    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 3


