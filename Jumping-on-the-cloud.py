'''
For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

Example
Index the array from 0....6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. 
They could follow these two paths: 0-2-4-6 or 0-2-3-4-6. 
The first path takes 4 jumps while the second takes 3. Return 3.

Function Description
Complete the jumpingOnClouds function in the editor below.
jumpingOnClouds has the following parameter(s):
int c[n]: an array of binary integers

Returns
int: the minimum number of jumps required
'''
from collections import deque


def jumping_on_the_clouds(c):
    q = deque()
    result_ways = 0
    for i in c:
        if len(q) > 0:
            if 0 == q.pop() and 0 == i:
                result_ways += 1
            elif 1 == q.pop() and 0 == i:
                pass
        q.append(i)


jumping_on_the_clouds([0, 0, 1, 0, 0, 1, 0])
