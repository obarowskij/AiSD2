from math import ceil
import heapq

class PathNotFoundException(Exception):
    pass 

class Node:
    def __init__(self,name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name
    
    def __hash__(self):
        return hash(self.name)

class Edge:
    def __init__(self,froom,to,cost,flow):
        self.froom = froom
        self.to = to
        self.cost = cost
        self.flow = flow

    def __str__(self):
        return f'{self.froom.name} {self.to.name} {self.cost} {self.flow}'
    
    def delete_edge(self):
        self.cost = 99999 
    
class Graf:
    def __init__(self):
        self.Nodes = []
        self.Edges = []
        self.max_value = 0


    def add_node(self,Node):
        self.Nodes.append(Node)


    def add_edge(self,Edge):
        self.Edges.append(Edge)
        self.max_value += Edge.flow

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph.Nodes}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()
    previous_nodes = {}
    previous_edges = {}
    min_flow = float('inf')  # Initialize min_flow to infinity

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_node in visited:
            continue

        visited.add(current_node)

        for edge in graph.Edges:
            if edge.froom == current_node:
                neighbor = edge.to
                distance = current_distance + edge.cost

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    previous_edges[neighbor] = edge
                    heapq.heappush(queue, (distance, neighbor))

    if end not in previous_nodes:
        raise PathNotFoundException("No path found")
    
    path_nodes = []
    path_edges = []
    current = end
    while current is not None:
        path_nodes.append(current)
        if current != start:
            path_edges.append(previous_edges[current])
            # Update min_flow with the minimum flow found so far
            min_flow = min(min_flow, previous_edges[current].flow)
        current = previous_nodes.get(current)
    path_nodes.reverse()
    path_edges.reverse()
    return distances[end], path_nodes, path_edges, min_flow

def dinic(G, start_node, end_node):
    path_available = True
    max_flow = 0
    cost = 0
    while path_available:
        try:
            lowest_cost, path_nodes, path_edges, min_flow = dijkstra(G, start_node, end_node)
            return lowest_cost
            if min_flow == 0:
                raise PathNotFoundException("No path found")
            
            for edge in path_edges:
                cost += edge.cost * min_flow
                edge.flow -= min_flow
                if edge.flow == 0:
                    edge.delete_edge()
            max_flow += min_flow
        except PathNotFoundException:
            path_available = False
            return cost


def calculate_distance(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

def calculate_cost(hull_points, world_points, pairs, neighbors):
    distances = []
    graph = Graf()
    graph.add_node(Node('factory'))
    for i in range(len(world_points)):
        graph.add_node(Node(str(i)))
    for elem in neighbors:
        graph.add_edge(Edge(graph.Nodes[elem[0]], graph.Nodes[elem[1]], elem[2], 99999))
    try:
        for i in range(len(hull_points)):
            distances.append(ceil(calculate_distance(hull_points[i], hull_points[i+1])))
    except IndexError:
        distances.append(ceil(calculate_distance(hull_points[i], hull_points[0])))
    
    cost = 0
    for i in range(len(hull_points)):
        index = world_points.index(hull_points[i])
        distance = dinic(graph, graph.Nodes[0], graph.Nodes[index+1])
        cost += (distance * distances[i])/pairs
    return cost

neighbors = [[0, 16, 29], [0, 3, 65], [0, 8, 65], [0, 17, 92], [16, 10, 149], [16, 8, 83], [16, 3, 82], [16, 11, 137], [3, 17, 108], [3, 11, 137], [3, 15, 120], [11, 4, 142], [11, 12, 140], [11, 10, 102], [11, 15, 179], [15, 17, 201], [15, 2, 124], [15, 14, 57], [15, 12, 125], [4, 1, 81], [4, 12, 100], [4, 10, 213], [4, 6, 63], [4, 13, 80], [12, 13, 77], [12, 5, 30], [12, 14, 117], [14, 2, 109], [14, 9, 76], [14, 7, 71], [14, 5, 122], [6, 13, 67], [6, 1, 22], [13, 7, 157], [13, 5, 56], [13, 1, 86], [5, 7, 118]]
hull_points = [[-187, 65], [-149, 144], [-114, 184], [136, 118], [168, 71], [102, -148], [-185, -176]]
world_points = [[-185, -176], [-114, 184], [57, 44], [-111, -142], [-142, -44], [-172, -158], [-187, 65], [168, 71], [-149, 144], [102, -148], [20, -88], [-112, -42], [-172, -91], [-117, 75], [-60, 72], [126, -1], [136, 118]]
pairs = 5
print(calculate_cost(hull_points, world_points, pairs, neighbors))
