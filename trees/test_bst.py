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
    
    def test_get_maximum(self):
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

    def test_get_minimum(self):
        bst = BST[int]()
        # if we inserted 5,2,1,3,7,6,8
        # bst should Look like this:
        #            5
        #        2		7
        #    1	  3	  6    8
        bst.insert(5)
        bst.insert(2)
        bst.insert(7)

        minimum = bst.get_minimum()
        assert minimum == 2, errors.wrong_value(minimum, 2)
        
        bst.insert(3)
        bst.insert(1)

        minimum = bst.get_minimum()
        assert minimum == 1, errors.wrong_value(minimum, 1)

        bst.insert(6)
        bst.insert(8)

        minimum = bst.get_minimum()
        assert minimum == 1, errors.wrong_value(minimum, 1)

    def test_delete(self):
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

        deleted1 = bst.delete(10)
        assert deleted1 is False, "Should be False"

        deleted2 = bst.delete(2)
        assert deleted2 is True, "Should be True"
        assert bst.search(2) is None, "Should be None"
        assert bst.get_size() == 6, "Size should be 6"
        replacement = bst.get_root().left
        assert replacement.val == 1, errors.wrong_value(replacement.val, 1)
        assert replacement.right.val == 3, errors.wrong_value(replacement.right.val, 3)

        deleted3 = bst.delete(1)
        assert deleted3 is True, "Should be True"
        assert bst.search(1) is None, "Should be None"
        assert bst.get_size() == 5, "Size should be 5"
        replacement2 = bst.get_root().left
        assert replacement2.val == 3, errors.wrong_value(replacement2.val, 3)
        assert replacement2.right is None, "Should be None"


        assert bst.delete(0) is False, "Should be False"
        assert bst.get_size() == 5, "Size should be 5"

        deleted4 = bst.delete(3)
        assert deleted4 is True, "Should be True"
        assert bst.search(3) is None, "Should be None"
        assert bst.get_size() == 4, "Size should be 4"
        replacement3 = bst.get_root().left
        assert replacement3 is None, "Should be None"


        deleted5 = bst.delete(7)
        assert deleted5 is True, "Should be True"
        assert bst.search(7) is None, "Should be None"
        assert bst.get_size() == 3, "Size should be 3"
        replacement4 = bst.get_root().right
        assert replacement4.val == 6, errors.wrong_value(replacement4.val, 6)
        assert replacement4.left is None, "Should be None"
        assert replacement4.right.val == 8, errors.wrong_value(replacement4.right.val, 8)  

        deleted6 = bst.delete(8)
        assert deleted6 is True, "Should be True"
        assert bst.search(8) is None, "Should be None"
        assert bst.get_root().right.right is None, "Should be None"

        deleted7 = bst.delete(5)
        assert deleted7 is True, "Should be True"
        assert bst.search(5) is None, "Should be None"
        assert bst.get_root().val == 6, errors.wrong_value(bst.get_root().val, 6)

    def test_BFT(self):
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

        assert bst.BFT() == [5, 2, 7, 1, 3, 6, 8], errors.wrong_value(bst.BFT(), [5, 2, 7, 1, 3, 6, 8])

    def test_BFS(self):
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

        assert bst.BFS(10) is None, "Should be None"
        two = bst.BFS(2)
        assert two.val == 2, errors.wrong_value(two.val, 2)
        assert two.left.val == 1, errors.wrong_value(two.left.val, 1)
        assert two.right.val == 3, errors.wrong_value(two.right.val, 3)

        seven = bst.BFS(7)
        assert seven.val == 7, errors.wrong_value(seven.val, 7)
        assert seven.left.val == 6, errors.wrong_value(seven.left.val, 6)
        assert seven.right.val == 8, errors.wrong_value(seven.right.val, 8)

        one = bst.BFS(1)
        assert one.val == 1, errors.wrong_value(one.val, 1)
        assert one.left is None and one.right is None, "Shouldn't have children"

        six = bst.BFS(6)
        assert six.val == 6, errors.wrong_value(six.val, 6)
        assert six.left is None and six.right is None, "Shouldn't have children"


    def test_DFT(self):
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

        preOrderTraversal = bst.DFT('preOrder')
        assert preOrderTraversal == [5, 2, 1, 3, 7, 6, 8], errors.wrong_value(preOrderTraversal, [5, 2, 1, 3, 7, 6, 8])

        inOrderTraversal = bst.DFT('inOrder')
        assert inOrderTraversal == [1, 2, 3, 5, 6, 7, 8], errors.wrong_value(inOrderTraversal, [1, 2, 3, 5, 6, 7, 8])

        postOrderTraversal = bst.DFT('postOrder')
        assert postOrderTraversal == [1, 3, 2, 6, 8, 7, 5], errors.wrong_value(postOrderTraversal, [1, 3, 2, 6, 8, 7, 5])

    def test_DFS(self):
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
        assert bst.DFS(2, 'preOrder') == two, "Not the right node"
        assert bst.DFS(2, 'inOrder') == two, "Not the right node"
        assert bst.DFS(2, 'postOrder') == two, "Not the right node"

        seven = bst.search(7)
        assert bst.DFS(7, 'preOrder') == seven, "Not the right node"
        assert bst.DFS(7, 'inOrder') == seven, "Not the right node"
        assert bst.DFS(7, 'postOrder') == seven, "Not the right node"

        eight = bst.search(8)
        assert bst.DFS(8, 'preOrder') == eight, "Not the right node"
        assert bst.DFS(8, 'inOrder') == eight, "Not the right node"
        assert bst.DFS(8, 'postOrder') == eight, "Not the right node"

        three = bst.search(3)
        assert bst.DFS(3, 'preOrder') == three, "Not the right node"
        assert bst.DFS(3, 'inOrder') == three, "Not the right node"
        assert bst.DFS(3, 'postOrder') == three, "Not the right node"