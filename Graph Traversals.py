from Stack import Stack


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


if __name__ == '__main__':
    graph = {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }
    dfs(graph, 'a')
