'''
Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.
'''


def connected_components_count(graph):
    count = 0
    visited = set()
    # Get the neighbors of all nodes
    for node in graph:
        if explore_nodes(graph, node, visited) == True:
            count += 1
    return count


def explore_nodes(graph, node, visited):
    # check if node is visited
    if str(node) in visited:
        return False

    # In the visited set, same node is being stored as int and str so, to avoid duplicates we are using str(node)
    visited.add(str(node))

    # traverse through the neighbor nodes
    for neighbor in graph[node]:
        explore_nodes(graph, neighbor, visited)

    return True


if __name__ == '__main__':
    graph = {
        0: [4, 7],
        1: [],
        2: [],
        3: [6],
        4: [0],
        6: [3],
        7: [0],
        8: []
    }
    print(connected_components_count(graph))
