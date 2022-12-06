import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='y', node_size=800)

pos = nx.spring_layout(G)
nx.draw_network_nodes(G, pos, nodelist=[1, 4, 3, 8, 9], wit_labels=True, node_color='g', node_size=1300)
nx.draw_network_nodes(G, pos, nodelist=[2, 5, 6, 7], wit_labels=True, node_color='r', node_size=1300)


graph = {'Amin': {'Wasim', 'Nick', 'Mike'},
         'Wasim': {'Imran', 'Amin'},
         'Imran': {'Wasim', 'Faras'},
         'Faras': {'Imran'},
         'Mike': {'Amin'},
         'Nick': {'Amin'}
         }


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for nextg in graph[start] - visited:
        dfs(graph, nextg, visited)
    return visited

