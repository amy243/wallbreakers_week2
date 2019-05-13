'''
link: https://leetcode.com/problems/isomorphic-strings
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        j=0
        for i in s:
            if i not in d and t[j] not in d.values():
                d[i]=t[j]
            j+=1
        st=''

        for i in s:
            if i in d:
                st+=(d[i])
        if t==st:
            #print('y')
            return True
        else:
            #print('n')
            return False
