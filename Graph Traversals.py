from Stack import Stack
from Queue import Queue


def dfs(graph, source):
    # initialize stack and push the source
    s = Stack()
    s.push(source)

    # iterate through graph till the stack size becomes 0
    while(s.size() > 0):
        # pop the stack
        current = s.pop()
        print(current)
        # get the neighbors of current node, push them to stack
        for neighbor in graph[current]:
            s.push(neighbor)


def dfs_recursive(graph, source):
    print(source)
    # recursive call on all neighbors of source
    for neighbor in graph[source]:
        dfs_recursive(graph, neighbor)


def bfs(graph, source):
    # initialize the queue
    q = Queue()
    q.enqueue(source)

    # iterate through graph till the queue size becomes 0
    while(q.size() > 0):
        # dequeue the queue
        current = q.dequeue()
        print(current)
        # get the neighbors of current node, enqueue them to Queue
        for neighbor in graph[current]:
            q.enqueue(neighbor)


if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    # dfs(graph, 'a')  # abdfce
    # print('********')
    # dfs_recursive(graph, 'a')  # acebdf
    # print('********')
    bfs(graph, 'a')  # acbedf
