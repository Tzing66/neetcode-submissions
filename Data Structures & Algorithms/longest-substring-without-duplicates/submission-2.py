class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        c = set()
        longest = 0

        while r < len(s):
            if s[r] in c:
                c.remove(s[l])
                l += 1
            
            else :
                c.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
        
        return longest


        # for r in range(len(s)):

        #     while s[r] in c:
        #         c.remove(s[l])
        #         l +=1
            
        #     c.add(s[r])
        #     longest = max(longest, r - l + 1)

        # return longest
    

