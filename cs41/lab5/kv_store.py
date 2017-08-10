#!/usr/bin/env python3 -tt
import time

class TimedKVStore:
    def __init__(self):
        self.store = {}
    def put(self, key, value, time):
        if key in self.store:
            self.store[key].append((value, time))
        else:
            self.store[key] = [(value, time)]
    def get(self, key, time = None):
        if time == None:
            if key in self.store:
                return self.store[key][-1][0]
            else:
                return None
        else:
            if key in self.store:
                valueList = self.store[key]
                for val, stamp in reversed(valueList):
                    if stamp < time:
                        return val
                return None
            else:
                return None
    def remove(self, key, time = None):
        if time == None:
            del self.store[key]
        else:
            if key in self.store:
                self.store[key] = [(key, stamp)
                                   for (key, stamp) in self.store[key]
                                   if stamp > time]
                if len(self.store[key]) == 0:
                    del self.store[key]

