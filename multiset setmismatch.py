'''
link:https://leetcode.com/problems/set-mismatch
'''
class Solution(object):
    def findErrorNums(self, nums):

        ar=[]
        from collections import Counter
        c=Counter()
        for i in nums:
            c[i]+=1
            if c[i]==2:
                ar.append(i)
        for i in range(1,len(nums)+1):
            if i not in c:
                ar.append(i)
                return(ar)
