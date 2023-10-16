def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        2206
        """

        s=set(nums)

        for x in s :
            if nums.count(x)%2!=0:
                return False
        return True