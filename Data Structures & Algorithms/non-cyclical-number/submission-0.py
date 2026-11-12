class Solution:
    def isHappy(self, n: int) -> bool:
        arr=[]
        x=n
        while True:
            x=self.squares(x)
            if x==1:
                return True
            if x not in arr:
                arr.append(x)
            elif x in arr:
                return False




    def squares(self,x):
        sum=0
        while x:
            sum+=(x%10)**2
            x=x//10
        return sum

        