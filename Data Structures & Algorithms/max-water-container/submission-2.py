class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # area = 0
        # for i in range(len(heights)):

        #     j = len(heights) - 1

            
        #     while i < j:
        #         h = min(heights[i],heights[j])
        #         w = j-i

        #         area = max (area, h*w)
        #         j = j-1
        
        # return area

        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            h = min(heights[l], heights[r])
            w = r-l
            area = max(area, h*w)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area