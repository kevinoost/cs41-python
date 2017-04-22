#!/usr/bin/env python3 -tt

from bloom_filter import *
import unittest
import random
import sys, inspect

class SimpleBloomFilterTests(unittest.TestCase):
    def setUp(self):
        with open('/usr/share/dict/words', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.lines = [x.lower().rstrip() for x in lines]
        self.bf = BloomFilter()
        for word in self.lines:
            self.bf.insert(word)
    def test_get_no_false_negatives(self):
        self.assertTrue(all([word in self.bf for word in self.lines]))
    def test_get_few_false_positives(self):
        num_false_positives = 0
        num_trials = 10000
        for i in range(num_trials):
            random_string = ''.join(random.choice('0123456789ABCDEF')
                                    for j in range(16))
            if random_string in self.bf:
                num_false_positives = num_false_positives + 1
        false_positive_rate = num_false_positives / num_trials
        self.assertTrue(false_positive_rate < 0.02)

tests = [obj for (name, obj) in inspect.getmembers(sys.modules[__name__])
              if inspect.isclass(obj) and 'Test' in name]
testSuites = [unittest.TestLoader().loadTestsFromTestCase(test)
              for test in tests]
alltests = unittest.TestSuite(testSuites)
unittest.TextTestRunner(verbosity=2).run(alltests)



