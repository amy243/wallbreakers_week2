'''
link: https://leetcode.com/problems/find-the-difference
'''


class Solution(object):
    def findTheDifference(self, s, t):
        di=0
        for i in range(len(s)):
            di-=ord(s[i])
            di+=ord(t[i])
        di+=ord(t[len(t)-1])
        return(chr(di))
