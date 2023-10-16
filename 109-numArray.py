def separateDigits(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res=[]

        for x in nums:

            x=str(x)

            for i in x:

                res.append(int(i))

        return res

print(separateDigits(nums = [13,25,83,77]))

"""
Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
Example 2:

Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].
"""