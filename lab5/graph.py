#!/usr/bin/env python3 -tt

class Vertex:
    def __init__(self, name=""):
        self.name = name
        self.edges = set()
    def __str__(self):
        return "{} {}".format(self.name, str(self.edges))

class Edge:
    def __init__(self, start, end, cost=1.0, visited=False):
        self.start = start
        self.end = end
        self.cost = cost
        self.visited = visited
    def __str__(self):
        return "{} {} {} {}".format(self.start, self.end,
                                    self.cost, self.visited)

class SimpleGraph:
    def __init__(self):
        self.verts = set()
        self.edges = set()
    def add_vertex(self, v):
        self.verts.add(v)
    def add_edge(self, v1, v2):
        edge = Edge(v1, v2)
        v1.edges.add(edge)
        v2.edges.add(edge)
        self.edges.add(edge)
    def contains_vertex(self, v):
        return v in self.verts
    def get_neighbors(v):
        candidates = set([edge.start for edge in v.edges])
        candidates.update([edge.end for edge in v.edges])
        candidates.remove(v)
        return candidates
    def is_empty(self):
        return len(self.verts) == 0 and len(self.edges) == 0
    def size(self):
        return len(self.verts), len(self.edges)
    def remove_vertex(self, v):
        for edge in v.edges:
            if v == edge.start:
                edge.end.edges.remove(edge)
            else:
                edge.start.edges.remove(edge)
        self.verts.remove(v)
    def remove_edge(v1, v2):
        for edge in v1.edges:
            if edge.start == v1 and edge.end == v2:
                target_edge = edge
                break
        v1.remove(target_edge)
        v2.remove(target_edge)
    def is_neighbor(v1, v2):
        return any([edge.start == v2 or edge.end == v2 for edge in v1.edges])
    def clear_all():
        for edge in self.edges:
            vert.visited = False
    def is_reachable(v1, v2):
        edges_left = [edge for edge in v1.edges if edge.start == v1]
        while len(edges_left) > 0:
            edge = edges_left.pop()
            nextVisited = edge.end
            if edge.visited:
                break
            edge.visited = True
            elif nextVisited == v2:
                self.clear_all()
                return True
            else:
                edges_left.extend([edge for edge in nextVisited.edges
                                   if edge.start == nextVisited])

