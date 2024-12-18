from singly import Singly 

def test_singly():
    singlyList = Singly[int]()
    singlyList.add_last(1)
    singlyList.add_last(2)
    singlyList.add_last(3)
    
    assert singlyList.get_head().data == 1


