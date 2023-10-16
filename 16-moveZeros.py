def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums=list(nums)
        zero=nums.count(0)

        for i in range(zero):
                nums.remove(0)
        for i in range(zero):
                nums.append(0)
        
        return nums
        
    

ans=moveZeroes([0,0,1])
print(ans)



''''
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''