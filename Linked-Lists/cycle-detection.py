'''
To detect if the linked list have any cycle in it, we use cycle detection.
As the cycle in linked lists will result in infinite loop.

BRUTE-FORCE
To detect if there is a cycle in the linked list, we have to mark each node as visited and check if the node was already visited while traversing.

SUB-OPTIMAL 
To store each visited node in a set/dict, look for it while traversing the linked list. This was sub optimal as it is not an in-place solution.

OPTIMAL
Have two pointers each starting at head, one moving at step=1 and other step=2 pace, check if they meet at any of the nodes.

def hasCycle(ll, head):
    # Check if the length of ll is greater than 2
    fast,slow=head   
    while(fast is not None and fast.next is not None):
        slow=head.next
        fast=head.next.next
        if(slow == fast):
            return Fasle
    return True

How many pointers do we need to count the number of nodes in a cycle, using only constant auxiliary space?
2
'''
