class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        m1=self.findMin(nums[0:n//2])
        m2=self.findMin(nums[n//2:])
        return min(m1,m2)    