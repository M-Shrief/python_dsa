# Used mainly to launch the debugger in the IDE (vscodium) 
from linkedlist.doubly import Doubly


doublyList = Doubly[int]()
doublyList.add_first(1)
doublyList.add_first(2)
doublyList.add_first(3)

deleted1 = doublyList.delete_last()

# from numbers.sum import sum
# print(sum(1,2))