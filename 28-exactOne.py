def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for e in nums:
            if nums.count(e)==1:
                return e
            


ans=singleNumber([1,2,3,1,2,3,4])
print(ans)

"""
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: n
"""