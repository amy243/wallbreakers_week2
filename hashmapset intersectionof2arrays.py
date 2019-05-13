'''
link: https://leetcode.com/problems/intersection-of-two-arrays
'''


class Solution(object):
    def intersection(self, nums1, nums2):

        s=set()
        for i in nums1:
            s.add(i)
        a=[]
        for i in nums2:
            if i in s:
                if i not in a:
                    a.append(i)
        return a
