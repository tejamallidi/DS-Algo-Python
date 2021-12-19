'''
Write a fucntion, has_path, that takes an adjacency list of a directed, acyclic graph and two nodes(src,dst). The function should return a boolean to determine whether there exists a pth between src and dst.
'''
from Stack import Stack
from Queue import Queue

# Using DFS


def has_path(graph, src, dst):
    # check the corner condition
    if src == dst:
        return True

    # traverse to neighbor and implement recursion
    for neighbor in graph[src]:
        # if it finds the path it will return True
        if has_path(graph, neighbor, dst) == True:
            return True
        # else let the recursion happen till the last node
    return False


def has_path_iteration(graph, src, dst):
    # handle the corner condition
    if src == dst:
        return True
    s = Stack()
    s.push(src)

    # traverse through the stack till size == 0
    while(s.size() > 0):
        current = s.pop()
        for neighbor in graph[current]:
            s.push(neighbor)
            if neighbor == dst:
                return True
    return False


# Using BFS
def has_path(graph, src, dst):
    # handle the corner case
    if src == dst:
        return True

    q = Queue()
    q.enqueue(src)

    # traverse through the queue till size == 0
    while(q.size() > 0):
        current = q.dequeue()
        # traverse through the neignbor nodes of current
        for neighbor in graph[current]:
            q.enqueue(neighbor)
            if neighbor == dst:
                return True
    return False


if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    print(has_path(graph, 'f', 'a'))
    # print(has_path_iteration(graph, 'f', 'a'))
