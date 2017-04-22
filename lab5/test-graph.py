#!/usr/bin/env python3 -tt

import unittest
import math
import sys, inspect
from graph import SimpleGraph
from graph import Vertex
from graph import Edge

class SimpleGraphTests(unittest.TestCase):
    def setUp(self):
        self.g = SimpleGraph()
        self.a = Vertex('a')
        self.b = Vertex('b')
        self.c = Vertex('c')
        self.d = Vertex('d')
        self.e = Vertex('e')
        self.f = Vertex('f')
        self.g.add_vertex(self.a)
        self.g.add_vertex(self.b)
        self.g.add_vertex(self.c)
        self.g.add_vertex(self.d)
        self.g.add_vertex(self.e)
        self.g.add_edge(self.a, self.b)
        self.g.add_edge(self.b, self.c)
        self.g.add_edge(self.c, self.b)
        self.g.add_edge(self.c, self.d)
    
    def test_is_empty(self):
        self.assertFalse(self.g.is_empty())
        self.g.remove_edge(self.a, self.b)
        self.g.remove_edge(self.b, self.c)
        self.g.remove_edge(self.c, self.b)
        self.g.remove_edge(self.c, self.d)
        self.g.remove_vertex(self.a)
        self.g.remove_vertex(self.b)
        self.g.remove_vertex(self.c)
        self.g.remove_vertex(self.d)
        self.g.remove_vertex(self.e)
        self.assertTrue(self.g.is_empty())
    
    def test_contains_vertex(self):
        self.assertTrue(self.g.contains_vertex(self.a))
        self.assertFalse(self.g.contains_vertex(self.f))
        
    def test_size(self):
        self.assertTrue(self.g.size() == (5, 4))
        self.g.add_edge(self.a, self.e)
        self.assertTrue(self.g.size() == (5, 5))
        self.g.remove_edge(self.a, self.e)
        self.assertTrue(self.g.size() == (5, 4))
        self.g.add_edge(self.a, self.b)
        self.assertTrue(self.g.size() == (5, 4))
        
    def test_get_neighbors(self):
        b_neighbors = self.g.get_neighbors(self.b)
        self.assertTrue(len(b_neighbors) == 2)
        self.assertTrue(self.a in b_neighbors)
        self.assertTrue(self.c in b_neighbors)
        self.assertTrue(self.g.is_neighbor(self.a, self.b))
        self.assertFalse(self.g.is_neighbor(self.a, self.d))
        self.assertTrue(all([not self.g.is_neighbor(self.e, v) for v in self.g.verts]))
        self.g.add_vertex(self.f)
        self.assertTrue(len(self.g.get_neighbors(self.f)) == 0)
        
    def test_is_reachable(self):
        self.assertTrue(self.g.is_reachable(self.a, self.d))
        self.assertTrue(self.g.is_reachable(self.a, self.d))
        self.assertFalse(self.g.is_reachable(self.d, self.a))
        self.assertFalse(self.g.is_reachable(self.a, self.e))
        self.g.remove_vertex(self.b)
        self.assertTrue(self.g.size() == (4, 1))
        self.assertFalse(self.g.is_reachable(self.a, self.d))

class IsBipartiteTests(unittest.TestCase):
    def setUp(self):
        self.b = SimpleGraph()
        self.l1 = Vertex('l1')
        self.l2 = Vertex('l2')
        self.l3 = Vertex('l3')
        self.l4 = Vertex('l4')
        self.r1 = Vertex('r1')
        self.r2 = Vertex('r2')
        self.r3 = Vertex('r3')
        self.b.add_vertex(self.l1)
        self.b.add_vertex(self.l2)
        self.b.add_vertex(self.l3)
        self.b.add_vertex(self.r1)
        self.b.add_vertex(self.r2)
        self.b.add_edge(self.l1, self.r1)
        self.b.add_edge(self.l1, self.r2)
        self.b.add_edge(self.l2, self.r1)
        self.b.add_edge(self.l2, self.r2)
        self.b.add_edge(self.l3, self.r1)
        self.b.add_edge(self.l3, self.r2)
        
    def test_is_bipartite(self):
        self.assertTrue(self.b.is_bipartite())
        self.bl1 = Vertex('bl1')
        self.bl2 = Vertex('bl2')
        self.br1 = Vertex('br1')
        self.b.add_vertex(self.bl1)
        self.b.add_vertex(self.bl2)
        self.b.add_vertex(self.br1)
        self.b.add_edge(self.bl1, self.br1)
        self.b.add_edge(self.bl2, self.br1)
        self.assertTrue(self.b.is_bipartite())
        
    def test_is_not_bipartite(self):
        self.c1 = Vertex('c1')
        self.b.add_vertex(self.c1)
        self.b.add_edge(self.l1, self.c1)
        self.b.add_edge(self.r1, self.c1)
        self.assertFalse(self.b.is_bipartite())

class DijkstrasAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.dg = SimpleGraph()
        self.one = Vertex('one')
        self.two = Vertex('two')
        self.three = Vertex('three')
        self.four = Vertex('four')
        self.five = Vertex('five')
        self.six = Vertex('six')
        self.disconnected = Vertex('disconnected')
        self.dg.add_vertex(self.one)
        self.dg.add_vertex(self.two)
        self.dg.add_vertex(self.three)
        self.dg.add_vertex(self.four)
        self.dg.add_vertex(self.five)
        self.dg.add_vertex(self.six)
        self.dg.add_vertex(self.disconnected)
        self.dg.add_edge(self.one, self.two, 7.0)
        self.dg.add_edge(self.two, self.one, 7.0)
        self.dg.add_edge(self.one, self.six, 14.0)
        self.dg.add_edge(self.six, self.one, 14.0)
        self.dg.add_edge(self.one, self.three, 9.0)
        self.dg.add_edge(self.three, self.one, 9.0)
        self.dg.add_edge(self.two, self.three, 10.0)
        self.dg.add_edge(self.three, self.two, 10.0)
        self.dg.add_edge(self.two, self.four, 15.0)
        self.dg.add_edge(self.four, self.two, 15.0)
        self.dg.add_edge(self.three, self.four, 11.0)
        self.dg.add_edge(self.four, self.three, 11.0)
        self.dg.add_edge(self.three, self.six, 2.0)
        self.dg.add_edge(self.six, self.three, 2.0)
        self.dg.add_edge(self.four, self.five, 6.0)
        self.dg.add_edge(self.five, self.four, 6.0)
        self.dg.add_edge(self.five, self.six, 9.0)
        self.dg.add_edge(self.six, self.five, 9.0)
    def test_dijkstras_algo(self):
        self.assertTrue(
            self.dg.dijkstras_algorithm(self.one, self.five)
            == (20.0, [self.one, self.three, self.six, self.five]))
    def test_dijkstras_unconnected(self):
        self.assertTrue(
            self.dg.dijkstras_algorithm(self.one, self.disconnected)
            == (math.inf, []))

class LargestConnectedComponentTests(unittest.TestCase):
    def setUp(self):
        self.cc = SimpleGraph()
        self.a = Vertex('a')
        self.b = Vertex('b')
        self.c = Vertex('c')
        self.d = Vertex('d')
        self.e = Vertex('e')
        self.f = Vertex('f')
    def test_no_connected_components(self):
        self.assertTrue(self.cc.largest_connected_component() == 0)
    def test_single_vertex_cc(self):
        self.cc.add_vertex(self.a)
        self.cc.add_vertex(self.b)
        self.cc.add_vertex(self.c)
        self.assertTrue(self.cc.largest_connected_component() == 1)
    def test_cc_of_size_3(self):
        self.cc.add_vertex(self.a)
        self.cc.add_vertex(self.b)
        self.cc.add_vertex(self.c)
        self.cc.add_vertex(self.d)
        self.cc.add_vertex(self.e)
        self.cc.add_vertex(self.f)
        self.cc.add_edge(self.a, self.b)
        self.cc.add_edge(self.a, self.c)
        self.cc.add_edge(self.d, self.e)
        self.assertTrue(self.cc.largest_connected_component() == 3)

tests = [obj for (name, obj) in inspect.getmembers(sys.modules[__name__])
              if inspect.isclass(obj) and 'Test' in name]
testSuites = [unittest.TestLoader().loadTestsFromTestCase(test)
              for test in tests]
alltests = unittest.TestSuite(testSuites)
unittest.TextTestRunner(verbosity=2).run(alltests)

