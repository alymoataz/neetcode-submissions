class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        output=[]
        for i in range(n):
            target=-nums[i]
            seen={}
            for j in range(i+1,n):
                if target-nums[j] in seen:
                    if sorted([nums[i],nums[j],target-nums[j]]) not in output:
                        output.append(sorted([nums[i],nums[j],target-nums[j]]))
                else:
                    seen[nums[j]]=1
        return output                    