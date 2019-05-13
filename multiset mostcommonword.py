'''
link: https://leetcode.com/problems/most-common-word
'''

class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        from collections import Counter
        c=Counter()
        p1=''
        for i in paragraph:
            if i in ("!?',;."):
                p1+=' '
            else:
                p1+=i

        p=p1.lower().split()
        print(p)
        for i in p:
            if i not in banned:

                c[i]+=1
        j=max(c.values())
        for i in c:
            if (c[i]==j):
                return(i)

