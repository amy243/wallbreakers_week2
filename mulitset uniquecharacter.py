'''
link: https://leetcode.com/problems/first-unique-character-in-a-string
'''
class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        st = Counter(s)
        for i in range(len(s)):
            t = s[i]
            if st.get(t)==1:
                return i
        else:
            return -1
