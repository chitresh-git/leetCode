

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
def demo(nums,target):
  for i in range(0,len(nums)-1):
             for j in range(i+1,len(nums)):
          
               if nums[i] +nums[j]==target:
               
                   l=[i,j]
                   return l
        
l=[12,3,4,5,6]
targ=int(input("enter the target value "))

print(demo(l,targ))
