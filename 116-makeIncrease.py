def minOperations(nums):
        """
        :type nums: List[int]
        :rtype: int
        1827
        """

        count=0

        for i in range(len(nums)-1):
                
                if nums[i]>=nums[i+1]:
                        count+=(nums[i]+1)-nums[1+i]
                        nums[i+1]=nums[i]+1

        
        return count

print(minOperations([1,1,1]))
"""

Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
Example 2:

Input: nums = [1,5,2,4,1]
Output: 14
Example 3:

Input: nums = [8]
Output: 0
"""

        