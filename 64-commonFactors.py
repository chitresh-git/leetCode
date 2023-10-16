def commonFactors(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        if a>b:
            temp=b
        else:
            temp=a

        count=0
        for e in range(1,temp+1):
            if a%e==0 and b%e==0:
                count+=1
        
        return count


ans=commonFactors(12,6)
print(ans)
