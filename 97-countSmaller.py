def smallerNumbersThanCurrent( nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res=[]

        for e  in nums:

            temp=[x for x in nums if e> x]

            res.append(len(temp))

        
        return res


ans=smallerNumbersThanCurrent(nums = [8,1,2,2,3])
print(ans)