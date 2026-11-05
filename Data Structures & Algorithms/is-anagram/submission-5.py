class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        for i in range(len(s)//2):
            s_d[i] = s[i]
            d_t[len(s) - i] = t[i]
            
        if s_d == d_t:
            return True
        else:
            return False