from .bst import BST
from ..utils import errors

class TestBST:

    def test_insert(self):
        bst = BST[int]()
        # if we inserted 5,2,1,3,7,6,8
        # bst should Look like this:
        #            5
        #        2		7
        #    1	  3	  6    8
        bst.insert(5)
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.insert(7)
        bst.insert(6)
        bst.insert(8)

        assert bst.get_size() == 7, "Size should be 7"

        root = bst.get_root()
        assert root.val == 5, errors.wrong_value(root.val, 5)

        assert root.left.val == 2, errors.wrong_value(root.left.val, 2)
        assert root.right.val == 7, errors.wrong_value(root.right.val, 7)

        assert root.left.left.val == 1, errors.wrong_value(root.left.left.val, 1)
        assert root.left.right.val == 3, errors.wrong_value(root.left.right.val, 3)

        assert root.right.left.val == 6, errors.wrong_value(root.right.left.val, 6)
        assert root.right.right.val == 8, errors.wrong_value(root.right.right.val, 8)
    
    def test_search(self):
        bst = BST[int]()
        # if we inserted 5,2,1,3,7,6,8
        # bst should Look like this:
        #            5
        #        2		7
        #    1	  3	  6    8
        bst.insert(5)
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.insert(7)
        bst.insert(6)
        bst.insert(8)

        two = bst.search(2)
        assert two.val == 2, errors.wrong_value(two.val, 2)
        assert two.left.val == 1, errors.wrong_value(two.val, 1)
        assert two.right.val == 3, errors.wrong_value(two.val, 3)

        six = bst.search(6)
        assert six.val == 6, errors.wrong_value(six.val, 6)

    def test_get_parent(self):
        bst = BST[int]()
        # if we inserted 5,2,1,3,7,6,8
        # bst should Look like this:
        #            5
        #        2		7
        #    1	  3	  6    8
        bst.insert(5)
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.insert(7)
        bst.insert(6)
        bst.insert(8)

        five = bst.get_parent(2)
        assert five.val == 5, errors.wrong_value(five.val, 5)
        five = bst.get_parent(7)
        assert five.val == 5, errors.wrong_value(five.val, 5)

        two = bst.get_parent(1)
        assert two.val == 2, errors.wrong_value(two.val, 2)
        two = bst.get_parent(3)
        assert two.val == 2, errors.wrong_value(two.val, 2)

        seven = bst.get_parent(6)
        assert seven.val == 7, errors.wrong_value(seven.val, 7)
        seven = bst.get_parent(8)
        assert seven.val == 7, errors.wrong_value(seven.val, 7)
    
    def test_maximum(self):
        bst = BST[int]()
        # if we inserted 5,2,1,3,7,6,8
        # bst should Look like this:
        #            5
        #        2		7
        #    1	  3	  6    8
        bst.insert(5)
        bst.insert(2)
        bst.insert(1)

        maximum = bst.get_maximum()
        assert maximum == 5, errors.wrong_value(maximum, 5)
        
        bst.insert(3)
        bst.insert(7)

        maximum = bst.get_maximum()
        assert maximum == 7, errors.wrong_value(maximum, 7)

        bst.insert(6)
        bst.insert(8)

        maximum = bst.get_maximum()
        assert maximum == 8, errors.wrong_value(maximum, 8)
