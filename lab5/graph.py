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
                                   if edge.start == nextVisited
                                   and not edge.visited])
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
                neighbors = [e.start if e.start != v else e.end
                             for e in v.edges]
                for neighbor in neighbors:
                    if neighbor.color == v.color:
                        self.clear_all()
                        return False
                    if neighbor.color == 'gray':
                        stack.append((v.color, neighbor))
        self.clear_all()
        return True



