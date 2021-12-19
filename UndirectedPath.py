'''
Write a fucntion, undirected_path, that takes an array of edges for an undirected graph and two nodes(src,dst). The function should return a boolean to determine whether there exists a pth between src and dst.

We have to create an adjacency list from edges list
check the neighbors by keeping track of a visited node
'''


def undirected_path(edges, src, dst):
    # since we got the edges list - create an adjacency list from that
    graph = build_adjacency_list(edges)
    # As search 'in' set is O(1) in average case we can select a Set
    return has_path(graph, src, dst, set())


def has_path(graph, src, dst, visited):
    # handle the base condition
    if src == dst:
        return True

    # check if src node in visited set
    if src in visited:
        return False

    # else add it to visited set
    visited.add(src)

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst, visited) == True:
            return True
    return False


def build_adjacency_list(edges):
    graph = {}

    for edge in edges:  # edge = ['i','j']
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        # create two way link between nodes as it is a undirected graph
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


if __name__ == '__main__':
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    print(undirected_path(edges, 'i', 'n'))
