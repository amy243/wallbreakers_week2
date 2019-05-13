'''
link: https://leetcode.com/problems/find-all-anagrams-in-a-string
'''
class Solution(object):
    def findAnagrams(self, s, p):
        d={}
        d2={}

        word=[]

        if len(s)==len(p):
            if s==p:
                word.append(0)
                return word
        elif len(s)<len(p):
                return word
        else:

            for i in p:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            L=len(p)
            for i in range(len(s)-L+1):
                if s[i]in d:
                    for j in range(i,i+L):
                        if s[j] in d2:
                            d2[s[j]]+=1
                        else:
                            d2[s[j]]=1
                    if d2==d:
                        word.append(i)
                    d2.clear()
            return(word)
