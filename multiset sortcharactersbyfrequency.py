'''
link: https://leetcode.com/problems/sort-characters-by-frequency
'''


class Solution(object):
    def frequencySort(self, s):

        ar=''
        from collections import Counter
        c=Counter()

        for i in s:
            c[i]+=1


        p = c.most_common()

        for i in p:
            ar+=i[0]*i[1]
        return(ar)
        
