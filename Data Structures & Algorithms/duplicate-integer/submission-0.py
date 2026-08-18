class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # c = 0

        # for i in nums:
        #     for j in nums:
        #         if j == i:
        #             c = c+1
        #     if c > 1:
        #         return True
        #     else:
        #         c = 0
        
        # if c == 0 or c == 1:
        #     return False

        new_set = set(nums)
        return len(new_set) != len(nums)


        