# Used mainly to launch the debugger in the IDE (vscodium) 
from trees.bst import BST

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

bst.delete(10)
bst.delete(2)
bst.delete(1)

bst.get_root()