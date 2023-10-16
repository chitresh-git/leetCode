def sumOfSquares(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum=0

        for i in range(0,len(nums)):

            if len(nums)%(i+1)==0:

                sum+=nums[i]**2

        
        return sum


print(sumOfSquares(nums = [1,2,3,4]))

k="fdf"
k.re