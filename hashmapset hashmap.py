'''
link: https://leetcode.com/problems/design-hashmap
'''
class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key):
        if key in self.keys:
            return self.values[self.keys.index(key)]
        else:
            return -1

    def remove(self, key):
        if key in self.keys:
            del self.values[self.keys.index(key)]
            del self.keys[self.keys.index(key)]


