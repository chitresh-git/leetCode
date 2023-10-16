def hammingWeight(n):
        """
        :type n: int
        :rtype: int
        """

        n=list(str(n))
        print(n)
        res=n.count("1")
        return res

ans=hammingWeight("11111111111111111111111111111101")
print(ans)
