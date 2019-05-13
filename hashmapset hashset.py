'''
link: https://leetcode.com/problems/design-hashset/
'''

class MyHashSet(object):

    def __init__(self):

        self.table = [-1] * 1000000

    def add(self, key):
        self.table[key] = 1


    def remove(self, key):
        self.table[key] = -1


    def contains(self, key):
        if self.table[key] == 1:
            return True
        else:
            return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
