'''
link: https://leetcode.com/problems/happy-number
'''
class Solution(object):
    def isHappy(self, n):

        dic=set()

        def sq(nu) :
            nu=str(nu)
            m=0
            for i in nu:
                m+=int(i)*int(i)
            if m in dic:
                return (False)
            elif m==1:
                return (True)
            else:
                dic.add(m)
                b=m
                return(sq(b))
        return(sq(n))
