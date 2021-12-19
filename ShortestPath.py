'''
Write a function, shortestPath, that takes in an array of edges for an undirected graph and two nodes (src, dst). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.
'''
from Queue import Queue


def shortest_path(edges, src, dst):
    # since it is an edges list, build adjacency list from this
    graph = build_graph(edges)
    visited = set()
    q = Queue()
    q.enqueue([src, 0])
    visited.add(src)

    while(q.size() > 0):
        current, distance = q.dequeue()

        if current == dst:
            return distance

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.enqueue([neighbor, distance + 1])
    return -1


def build_graph(edges):
    graph = {}

    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph


if __name__ == '__main__':
    edges = [
        ['a', 'c'],
        ['a', 'b'],
        ['c', 'b'],
        ['c', 'd'],
        ['b', 'd'],
        ['e', 'd'],
        ['g', 'f']
    ]
    print(shortest_path(edges, 'a', 'e'))
