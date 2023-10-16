def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums=list(nums)

        low=0
        high=len(nums)-1

        left,right=0,0

        for i in range(len(nums)/2):
                left=left+nums[i]
                right=right+nums[high-i]


        