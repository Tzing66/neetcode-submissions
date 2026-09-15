class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums_sorted = sorted(set(nums))


        print(nums_sorted)
        

        #print(cons)
        #print(len(cons))

        c = 1
        l = 1

        for i in range(len(nums_sorted)-1):
            if nums_sorted[i] + 1 == nums_sorted[i+1]:
                c +=1
                l = max(l,c)
            else:
                c = 1
        
        return l

            
