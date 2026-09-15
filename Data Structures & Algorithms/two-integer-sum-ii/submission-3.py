class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for n1 in numbers:
        #     n2 = target - n1
        #     if n2 in numbers:
        #         return [numbers.index(n1)+1, numbers.index(n2)+1]
        
        l, r = 0, len(numbers) - 1

        while l<r:
            curr = numbers[l] + numbers[r]

            if curr == target :
                return [l+1,r+1]
            
            if curr < target:
                l += 1
            else:
                r -= 1
