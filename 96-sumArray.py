def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum,res=0,[]

        for e in nums:

            sum+=e
            res.append(sum)


        return res