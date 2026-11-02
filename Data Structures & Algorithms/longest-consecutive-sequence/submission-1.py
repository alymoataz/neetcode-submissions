class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        maxcount=0
        seen=set(nums)
        for num in nums:
            count=1
            if num-1 not in seen:
                currentnum=num
                while currentnum+1 in seen:
                    count+=1
                    currentnum+=1
                maxcount=max(maxcount,count)
        return maxcount           