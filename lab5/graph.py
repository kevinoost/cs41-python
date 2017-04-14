#!/usr/bin/env python3 -tt

class Vertex:
    def __init__(self, name="",color="gray"):
        self.name = name
        self.edges = set()
        self.color = color
    def __str__(self):
        return "[name={}, edges={}, color={}]".format(self.name, str(self.edges), self.color)
    def __repr__(self):
        return str(self)

class Edge:
    def __init__(self, start, end, cost=1.0, visited=False):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = visited
    def __str__(self):
        return "[({}->{}) cost={} v={}]".format(self.start.name, self.end.name,
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
        for vert in self.verts:
            vert.color = "gray"
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
    def is_bipartite(self):
        verts = set(self.verts)
        while len(verts) > 0:
            stack = list()
            v = verts.pop()
            
            stack.append(("black", v))
            while len(stack) > 0:
                par_color, v = stack.pop()
                if v in verts:
                    verts.remove(v)
                if v.color == par_color:
                    self.clear_all()
                    return False
                if v.color == "gray" and par_color == "black":
                    v.color = "red"
                elif v.color == "gray" and par_color == "red":
                    v.color = "black"
                neighbors = [e.start if e.start != v else e.end for e in v.edges]
                for neighbor in neighbors:
                    if neighbor.color == v.color:
                        self.clear_all()
                        return False
                    if neighbor.color == 'gray':
                        stack.append((v.color, neighbor))
        self.clear_all()
        return True

"""
from graph import SimpleGraph
from graph import Vertex
from graph import Edge
"""

g = SimpleGraph()
assert g.is_empty()

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')

g.add_vertex(a)
assert not g.is_empty()

g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)

assert g.contains_vertex(a)
assert not g.contains_vertex(f)

g.add_edge(a, b)
g.add_edge(a, e)
g.remove_edge(a, e)
assert g.size() == (5, 1)

g.add_edge(a, b)
assert g.size() == (5, 1)

g.add_edge(b, c)
g.add_edge(c, b)
g.add_edge(c, d)

b_neighbors = g.get_neighbors(b)
assert len(b_neighbors) == 2
assert a in b_neighbors
assert c in b_neighbors

assert g.is_neighbor(a, b)
assert not g.is_neighbor(a, d)
assert all([not g.is_neighbor(e, v) for v in g.verts])

assert g.is_reachable(a, d)
assert g.is_reachable(a, d)

assert not g.is_reachable(d, a)
assert not g.is_reachable(a, e)

g.remove_vertex(b)
assert g.size() == (4, 1)

b = SimpleGraph()
l1 = Vertex('l1')
l2 = Vertex('l2')
l3 = Vertex('l3')
l4 = Vertex('l4')
r1 = Vertex('r1')
r2 = Vertex('r2')
r3 = Vertex('r3')

b.add_vertex(l1)
b.add_vertex(l2)
b.add_vertex(l3)
b.add_vertex(l4)
b.add_vertex(r1)
b.add_vertex(r2)
b.add_vertex(r3)
b.add_edge(l1, r1)
b.add_edge(l1, r2)
b.add_edge(l1, r3)
b.add_edge(l2, r1)
b.add_edge(l2, r2)
b.add_edge(l2, r3)
b.add_edge(l3, r1)
b.add_edge(l3, r2)
b.add_edge(l3, r3)
b.add_edge(l4, r1)
b.add_edge(l4, r2)
b.add_edge(l4, r3)

assert b.is_bipartite()
bl1 = Vertex('bl1')
bl2 = Vertex('bl2')
br1 = Vertex('br1')
b.add_vertex(bl1)
b.add_vertex(bl2)
b.add_vertex(br1)
b.add_edge(bl1, br1)
b.add_edge(bl2, br1)
assert b.is_bipartite()

c1 = Vertex('c1')
b.add_vertex(c1)
b.add_edge(l1, c1)
b.add_edge(r1, c1)
assert not b.is_bipartite()

