class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:
            return 1
        fib=1
        prev=1
        next=0
        for i in range(2,n+1):
            next=fib+prev
            prev=fib
            fib=next
        return fib