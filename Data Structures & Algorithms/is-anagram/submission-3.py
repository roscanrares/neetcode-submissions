class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != t[i]:
                return True
        return False