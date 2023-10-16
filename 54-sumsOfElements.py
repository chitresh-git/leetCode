def differenceOfSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        arraySum=sum(nums)
        sumElements=0
      

        for out in nums:
                out=str(out)
                for inn in out:
                        sumElements=sumElements+int(inn)
                
        return arraySum-sumElements

ans=differenceOfSum([1,15,6,3])
print(ans)

