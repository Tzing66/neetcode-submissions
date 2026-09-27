class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count = {}
        # l = 0
        # max_freq = 0
        # longest = 0

        # for r in range(len(s)):
        #     count[s[r]] = count.get(s[r], 0) + 1
        #     max_freq = max(max_freq, count[s[r]])

        #     while (r - l + 1) - max_freq > k:
        #         count[s[l]] -= 1
        #         l += 1

        #     longest = max(longest, r - l + 1)

        # return longest

        left = 0
        longest = 0
        maxf = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            window = r-left+1
            while window - maxf > k: 
                count[s[left]] -= 1
                left += 1
                window -= 1
            longest = max(longest, window)

        return longest