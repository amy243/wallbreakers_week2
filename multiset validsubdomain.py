'''
link: https://leetcode.com/problems/subdomain-visit-count
'''

class Solution(object):
    def subdomainVisits(self, cpdomains):
        from collections import Counter
        c = Counter()
        for cd in cpdomains:
            n, d = cd.split(' ')
            c[d] += int(n)
            ar=[]

            for i in range(len(d)):
                if d[i] == '.':
                    c[d[i + 1:]] += int(n)
        for i in c:
            ar.append(str(c[i])+" "+str(i))
        return (ar)
