def sumZero(n):
        """
        :type n: int
        :rtype: List[int]
        """

        res=[]
        for i in range(1,n):
                res.append(i)
        
        s=sum(res)
        n=-s
        res.append(n)
        print(sum(res))
        return res

ans=sumZero(5)
print(ans)