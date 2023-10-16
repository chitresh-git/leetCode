def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits.reverse()
        sum,n=0,0
        for i in digits:
           sum=sum+ i*(10**n)
           n+=1
        
        sum+=1
        sum=list(str(sum))
        # sum=list(sum)
        sum=list(map(int,sum))
        # sum=list(sum)
        print(sum)

plusOne([1,2,3,4,9])