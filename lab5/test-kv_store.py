#!/usr/bin/env python3 -tt
from kv_store import *
import unittest
import sys, inspect

class SimpleKVStoreTests(unittest.TestCase):
    def setUp(self):
        self.kv = TimedKVStore()
        self.t0 = time.time()
        time.sleep(.001)
        self.kv.put("1", 1, time.time())
        self.kv.put("2", 2, time.time())
        self.kv.put("3", 3, time.time())
        time.sleep(.001)
        self.t1 = time.time()
        time.sleep(.001)
        self.kv.put("1", 1.1, time.time())
        time.sleep(.001)
        self.t2 = time.time()
    def test_get(self):
        self.assertTrue(self.kv.get("1") == 1.1)
        self.assertTrue(self.kv.get("1", self.t1) == 1)
        self.assertTrue(self.kv.get("1", self.t2) == 1.1)
    def test_remove(self):
        self.kv.remove("2")
        self.assertTrue(len(self.kv.store) == 2)
        self.kv.remove("3", self.t1)
        self.assertTrue(len(self.kv.store) == 1)
        self.kv.remove("1", self.t0)
        self.assertTrue(len(self.kv.store) == 1)
        self.assertTrue(len(self.kv.store["1"]) == 2)
        self.kv.remove("1", self.t1)
        self.assertTrue(len(self.kv.store) == 1)
        self.assertTrue(len(self.kv.store["1"]) == 1)
        self.kv.remove("1", self.t2)
        self.assertTrue(len(self.kv.store) == 0)

tests = [obj for (name, obj) in inspect.getmembers(sys.modules[__name__])
              if inspect.isclass(obj) and 'Test' in name]
testSuites = [unittest.TestLoader().loadTestsFromTestCase(test)
              for test in tests]
alltests = unittest.TestSuite(testSuites)
unittest.TextTestRunner(verbosity=2).run(alltests)

