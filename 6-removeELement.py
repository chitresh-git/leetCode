def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(nums)
        copy=nums
        s=set(copy)
        
        for e in s:
          if 1>nums.count(s):
               pass


temp=removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(temp)
      
