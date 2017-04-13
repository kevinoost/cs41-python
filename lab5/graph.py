#!/usr/bin/env python3 -tt

class Vertex:
    def __init__(self, name=""):
        self.name = name
        self.edges = set()
    def __str__(self):
        return "{} {}".format(self.name, str(self.edges))
    def __repr__(self):
        return str(self)

class Edge:
    def __init__(self, start, end, cost=1.0, visited=False):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = visited
    def __str__(self):
        return "{} {} {} {}".format(self.start.name, self.end.name,
                                    self.cost, self.visited)
    def __repr__(self):
        return str(self)

class SimpleGraph:
    def __init__(self):
        self.verts = set()
        self.edges = set()
    def __str__(self):
        return "{} {}".format(str(self.verts), str(self.edges))
    def __repr__(self):
        return str(self)
    def add_vertex(self, v):
        self.verts.add(v)
    def add_edge(self, v1, v2):
        for edge in self.edges:
            if edge.start == v1 and edge.end == v2:
                return
        edge = Edge(v1, v2)
        v1.edges.add(edge)
        v2.edges.add(edge)
        self.edges.add(edge)
    def contains_vertex(self, v):
        return v in self.verts
    def get_neighbors(self, v):
        candidates = set([edge.start for edge in v.edges])
        candidates.update([edge.end for edge in v.edges])
        candidates.remove(v)
        return candidates
    def is_empty(self):
        return self.size() == (0, 0)
    def size(self):
        return len(self.verts), len(self.edges)
    def remove_vertex(self, v):
        edge_list = list(v.edges)
        for edge in edge_list:
            self.remove_edge(edge.start,edge.end)
        self.verts.remove(v)
    def remove_edge(self, v1, v2):
        for edge in v1.edges:
            if edge.start == v1 and edge.end == v2:
                target_edge = edge
                break
        v1.edges.remove(target_edge)
        v2.edges.remove(target_edge)
        self.edges.remove(target_edge)
    def is_neighbor(self, v1, v2):
        return any([edge.start == v2 or edge.end == v2 for edge in v1.edges])
    def clear_all(self):
        for edge in self.edges:
            edge.visited = False
    def is_reachable(self, v1, v2):
        edges_left = [edge for edge in v1.edges if edge.start == v1]
        while len(edges_left) > 0:
            edge = edges_left.pop()
            nextVisited = edge.end
            if edge.visited:
                break
            edge.visited = True
            if nextVisited == v2:
                self.clear_all()
                return True
            else:
                edges_left.extend([edge for edge in nextVisited.edges
                                   if edge.start == nextVisited and not edge.visited])
        self.clear_all()
        return False

""""""
from graph import SimpleGraph
from graph import Vertex
from graph import Edge

g = SimpleGraph()
g.is_empty() == True
result = g.is_empty()

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')

g.add_vertex(a)
g.is_empty() == False
result = g.is_empty()

g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)

g.contains_vertex(a) == True
result = g.contains_vertex(a)
g.contains_vertex(f) == False
result = g.contains_vertex(f)

g.add_edge(a, b)
g.add_edge(a, e)
g.remove_edge(a, e)
g.size() == (5, 1)
result = g.size()

g.add_edge(a, b)
g.size() == (5, 1)
result = g.size()

g.add_edge(b, c)
g.add_edge(c, b)
g.add_edge(c, d)

b_neighbors = g.get_neighbors(b)
len(b_neighbors) == 2
result = len(b_neighbors)
a in b_neighbors
result = (a in b_neighbors)
c in b_neighbors
result = (c in b_neighbors)

g.is_neighbor(a, b) == True
result = g.is_neighbor(a, b)
g.is_neighbor(a, d) == False
result = g.is_neighbor(a, d)
all([not g.is_neighbor(e, v) for v in g.verts]) == True
result = all([not g.is_neighbor(e, v) for v in g.verts])

g.is_reachable(a, d) == True
result = g.is_reachable(a, d)
g.is_reachable(a, d) == True
result = g.is_reachable(a, d)

g.is_reachable(d, a) == False
result = g.is_reachable(d, a)

g.is_reachable(a, e) == False
result = g.is_reachable(a, e)

g.remove_vertex(b)
g.size() == (4, 1)
result = g.size()
result


""""""
