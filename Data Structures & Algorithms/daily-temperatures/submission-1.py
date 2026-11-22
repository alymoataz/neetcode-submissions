class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        results=[0]*n
        stack=[]
        stack.append((0,temperatures[0]))
        for i in range(1,n):
            while stack and temperatures[i]>stack[-1][1]:
                results[stack[-1][0]]=i-stack[-1][0]
                stack.pop()
            stack.append((i,temperatures[i]))
        return results
        
        
        