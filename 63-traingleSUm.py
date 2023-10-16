def triangularSum( nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums=list(nums)
        dummy=[]
        j=1

        while len(nums)!=1:

            for i in range(len(nums)-1):
                  sum=nums[i]+nums[i+1]
                  nums[i]=sum
            
            nums[:len(nums)-j]
            j+=1
            print(nums)
            
        
        print(nums)

triangularSum([1,2,3,4,5])

                