class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n

        fw = 1
        bw = 1

        for i in range (n):
            res[i] = fw
            fw *= nums[i]

        for i in range (n-1, -1, -1):
            res[i] *= bw
            bw *= nums[i]

        return res 
