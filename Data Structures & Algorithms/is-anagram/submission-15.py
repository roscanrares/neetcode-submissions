class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d_t = {}
        d_s = {}
        for i in range(len(s)):
            if s[i] in d_s: d_s[s[i]] += 1
            else: d_s[s[i]] = 1
            if t[i] in d_t: d_t[t[i]] += 1
            else: d_t[t[i]] = 1
        return d_s == d_t