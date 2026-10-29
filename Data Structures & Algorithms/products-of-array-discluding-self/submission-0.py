class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        n=len(nums)
        leftprod=[1]*n
        rightprod=[1]*n
        for i in range(1,n):
            leftprod[i]=nums[i-1]*leftprod[i-1]
        for i in range(n-2,-1,-1):
            rightprod[i]=rightprod[i+1]*nums[i+1]
        for i in range(n):
            output.append(leftprod[i]*rightprod[i])
        return output    

        
        