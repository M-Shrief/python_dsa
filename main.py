# Used mainly to launch the debugger in the IDE (vscodium) 
from linkedlist.singly import Singly


singlyList = Singly[int]()
singlyList.add_last(1)
singlyList.add_last(2)
singlyList.add_last(3)
singlyList.add_last(4)
singlyList.add_last(5)

singlyList.delete_by_index(2)
singlyList.delete_by_index(2)
singlyList.delete_by_index(2)

# from numbers.sum import sum
# print(sum(1,2))