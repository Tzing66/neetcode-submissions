class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d1, d2 = {}, {}

        for i in range (len(t)):
            ls = s[i]
            lt = t[i]

            if ls in d1:
                d1[ls] += 1
            else:
                d1[ls] = 1
            
            if lt in d2:
                d2[lt] += 1
            else:
                d2[lt] = 1
            
        return d1 == d2

        