'''
link: https://leetcode.com/problems/unique-morse-code-words
'''

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        dic={}
        mor=set()


        for j in range(26):
            dic[chr(97+j)]=morse[j]
        for word in words:
            w=""
            for j in word:
                w+=(dic[j])
            mor.add(w)
        return(len(mor))

