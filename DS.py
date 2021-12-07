'''
Array is equivalent to list in python
HashTable internals are being used by a dictionary in python
There is no specific linkedlist equivalent in python
'''
'''
BIG O NOTATION
Used to measure how the execution time changes based on an increase in the input's size
Ignore constant effort tasks and consider the fastest growing term
'''

'''
ARRAYS/LISTS
It is possible to store both strings and numbers in a same list in python but not possible in java/c++ 
'''
# list = ['Apple', 'Banana', 'Carrot', 'Dry fruits']
# num_list = [1, 3, 4, 5, 6]
# list.append('Egg Plant')
# num_list.insert(1, 2)
# num_list.append(7)
# # list.remove('Aple') # Gives ValueError as this element 'Aple' is not in list
# print(list)
# print(num_list)

'''
LINKED LIST
To overcome the memory issues of dynamic arrays/lists we go to linkedlists
Linkedlists will have "nodes" connected to each other 
Each node will have "data","next" 
Traversal is O(n)
insertion at first position is O(1)
deletion at first position is O(1)
insertion at last position is O(n)
deletion at last position is O(n)
If you know the index of the element, it is better to go with list
'''
