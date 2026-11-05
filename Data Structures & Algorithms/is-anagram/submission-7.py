class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        for i in range(len(s)//2):
            s_d[i] = s[i]
            t_d[len(s) - i] = t[i]
        
        if s_d == t_d:
            return False
        else:
            return True