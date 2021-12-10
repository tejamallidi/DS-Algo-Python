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

'''
HashMap/Dictionary
To find a record, it is efficient to use a dictionary
It will store the data in random memory locations using a hash function
Duplicate keys are not allowed in a dictionary
Lookup - O(1)
Insertion/Deletion - O(1)
'''
# stock_price = {}
# stock_price['dec 9'] = 147.29
# stock_price['dec 9'] = 148.39
# print(stock_price['Dec 9']) # this should throw KeyError as 'Dec 9' doesn't exist
# print(stock_price.get('Dec 9')) # this returns 'None' as 'Dec 9' doesn't exist
# Using del to remove a dict
# raises exception of KeyError if not found
# del stock_price['dec 9']
# print(stock_price)

# Using pop() to remove a dict pair
# it will not throw an error if we give a pair and key doesn't exist
# removed_value = stock_price.pop('dec 9', 'No Key found')
# print("The dictionary after remove is : " + str(stock_price))
# print("The removed key's value is : " + str(removed_value))


'''
Stack(LIFO)
Push/Pop element - O(1)
Search - O(n)
collections.deque(internally using doubly linked list) is used as stack in python 
As list uses dynamic resizing once it is full, it will waste lots of memory hence we don't use list as stack
'''
# stack = deque()
# stack.append('I am first item')
# stack.append('I am second item')
# stack.append('I am third item')
# stack.append('I am fourth item')
# stack.pop()
# print(stack)


'''
Queue(FIFO)
collections.deque(internally using doubly linked list) is used as queue in python
As list uses dynamic resizing once it is full, it will waste lots of memory hence we don't use list as queue
Access/Search - O(n)
Insertion/Deletion - O(1)
'''
# from collections import deque
# q = deque()
# q.appendleft(5)
# q.appendleft(6)
# q.appendleft(7)
# # q.pop()
# print(q)


'''
TREE
Best used to store info in a hierarchy 
example - folders,subfolders,files
Root Node --> Node
'''
