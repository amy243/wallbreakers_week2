'''
link: https://leetcode.com/problems/word-pattern
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        st=str.split()
        d={}
        if len(pattern)==len(st):
            for i in range(len(pattern)):
                if pattern[i] not in d and st[i] not in d.values():
                    d[pattern[i]]=st[i]
            ar=[]
            for i in pattern:
                if i in d:
                    ar.append(d[i])
                else:
                    return False
            if ar==st:
                return(True)
            else:
                return(False)
        else:
            return False
