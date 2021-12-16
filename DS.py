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

Binary Tree --> maximum of 2 children
left side - small elements than parent
right side - bug elements than parent
elements are always unique
Search, Insert, Delete  - O(log n)

To search in a BST - two traversal techniques
Breadth First Search(BFS)
Depth First Search(DFS)
 1. In order traversal
 2. Pre order traversal
 3. Post order traversal
BST looks like this - 15 root node
            15
    
    12              27     

7       14      20      88
                    
                    23

In order traversal: [7,12,14,15,20,23,27,88] - columns bottom to top (ascending order) left,root,right
Pre order traversal: [15,12,7,14,27,20,23,88] - root,left,right
Post order traversal:[7,14,12,23,20,88,27,15] - left,right,root
Binary tree is a special case of a general tree where you can have maximum 2 children for any given node.
They are useful in implementing set/map class in different programming languages. They provide efficient way of search an element in log n complexity. There are various traversal schemes you can use such as breadth first search and depth first search. In depth first search you can use in order traversal, pre order traversal and post order traversal schemes that will benefit in different scenarious. For example  in order traversal gives you a sorted list of elements in a tree. After going through theory we will implement binary tree, rather binary search tree in python. Binary search tree is also known as BST that is basically a binary tree with some order of elements.

Delete a node in a BST
Three cases to e considered
1. node with no child
2. node with one child
3. node with two children - find_min in the right subtree of that node or find_max from left subtree and copy minimum/maximum to the current position and delete the duplicate from right/left subtree
'''


'''
GRAPH
Directed or Undirected Data structures
Diff between tree and graph is the direction - Tree will have only one path between two nodes.
'''

'''
BINARY SEARCH
Works best on a sorted list
In k iterations, we will reduce the elements to be processed by n/2^k
Run time complexity to search for k will be O(log n) 
'''

'''
QUICK SORT - Divide and Conquer Type
Hoare Partition Scheme - left most element - pivot
Lomuto Partition Scheme - right most element - pivot
Select 1st index - pivot, put that in the correct position
such that left side elements < pivot, right side elements > pivot - Repeat this.
Putting the pivot in the right position - partition 
Two pointers - start, end. start will be looking for elements greater than pivot, end is looking for elements less than pivot, once we find them swap them.
'''
