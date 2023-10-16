def minOperations(n):
        """
        :type n: int
        :rtype: int
        """

        ans=0
        prev=0

        for i in range(1,n+1):
            ans=int(i/2)+prev
            prev=ans
            print(ans)

        return ans


ans=minOperations(7)

print(ans)
         