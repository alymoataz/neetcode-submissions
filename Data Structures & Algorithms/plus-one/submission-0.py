class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        s=0
        for i in range(n):
            s+=digits[i]*(10**(n-1-i))
        s+=1
        arr=[]
        while s:
            arr.append(s%10)
            s=s//10
        arr[:]=arr[::-1]
        return arr        
