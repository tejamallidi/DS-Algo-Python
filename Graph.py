class Graph:

    def __init__(self, edges):
        self.edges = edges
        # we have received a list of tuples, unpack them and convert them to a dict
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print('Graph Dict: ', self.graph_dict)

    def get_paths(self, start, end, path=[]):
        # Include the start city in the path
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            # check if node is already visited
            if node not in path:
                # get all the possible paths to end city from node
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path+[start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return []

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')
    ]

    route_graph = Graph(routes)
    # print(route_graph.get_paths('Mumbai', 'New York'))
    print(route_graph.get_shortest_path('Mumbai', 'New York'))
