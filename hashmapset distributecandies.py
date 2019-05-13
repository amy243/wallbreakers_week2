'''
link: https://leetcode.com/problems/distribute-candies
'''

class Solution(object):
    def distributeCandies(self, candies):

        s=set()
        for i in candies:
            s.add(i)
        return(min(len(s),len(candies)/2))
