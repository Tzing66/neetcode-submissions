from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window_count = Counter()

        for r in range(len(s2)):
            window_count[s2[r]] += 1

            l = r - len(s1)

            if l >= 0:
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]

            if window_count == s1_count:
                return True
        
        return False

