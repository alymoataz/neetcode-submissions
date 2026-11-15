class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            c=0
            while i:
                if i&1==1:
                    c+=1
                i//=2
            res.append(c)
        return res    

        