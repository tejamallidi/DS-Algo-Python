'''
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.
'''


def largest_component(graph):
    largest = 0
    visited = set()

    for node in graph:
        returned = explore_nodes(graph, node, visited)
        if returned > largest:
            largest = returned
    return largest


def explore_nodes(graph, node, visited):
    # check if node is visited
    if node in visited:
        return 0

    visited.add(node)

    # initialize count to 1 to count the 'node'
    count = 1
    # traverse through the neighbor nodes
    for neighbor in graph[node]:
        count += explore_nodes(graph, neighbor, visited)

    return count


if __name__ == '__main__':
    graph = {
        '3': [],
        '4': ['6'],
        '6': ['4', '5', '7', '8'],
        '8': ['6'],
        '7': ['6'],
        '5': ['6'],
        '1': ['2'],
        '2': ['1']
    }
    print(largest_component(graph))
