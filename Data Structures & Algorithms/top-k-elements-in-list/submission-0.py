class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        freq_sorted = dict(sorted(freq.items(), key = lambda item: item[1], reverse = True))

        l = []
        for i, key in enumerate(freq_sorted):
            if i >= k:
                break
            l.append(key)

        return l
        