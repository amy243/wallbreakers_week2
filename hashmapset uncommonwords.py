'''
link:https://leetcode.com/problems/uncommon-words-from-two-sentences
'''

class Solution(object):
    def uncommonFromSentences(self, A, B):

        a=A.split(' ')
        b=B.split(' ')
        dic={}

        for i in a:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1


        for j in b:
            if j not in dic:
                dic[j]=1
            else:
                dic[j]+=1

        aaa=[]
        for i in dic:
            if dic[i]==1:
                aaa.append(i)
        return(aaa)
