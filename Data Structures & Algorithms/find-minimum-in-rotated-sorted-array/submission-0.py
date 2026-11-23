class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_num=1000
        for num in nums:
            min_num=min(min_num,num)
        return min_num