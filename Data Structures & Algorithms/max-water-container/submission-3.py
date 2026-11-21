class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        maxarea=0
        while left<right:
            area=(right-left)*min(heights[left],heights[right])
            maxarea=max(maxarea,area)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return maxarea
            
