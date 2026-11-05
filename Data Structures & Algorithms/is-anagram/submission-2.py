class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)//2 +1):
            if s[i] != t[i]:
                return True
        return False