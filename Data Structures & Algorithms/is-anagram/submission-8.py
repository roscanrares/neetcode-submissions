class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 1: return True
        for i in range(len(s)//2):
            if s[i] != t[i]:
                return True
        return False