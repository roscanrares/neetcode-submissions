class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_t = {}
        d_s = {}
        for i in range(len(s)):
            if s[i] in d_s: d_s[i] += 1
            else: d_s[i] = 1
            if t[i] in d_s: d_t[i] += 1
            else: d_t[i] = 1