def findDifference(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        a,b=[],[]
        for e in nums1:
               if nums2.count(e)==0:a.append(e)
                        

        for e in nums2:
                if nums1.count(e)==0: b.append(e)
        
                       
        a,b=list(set(a)),list(set(b))
        

       

        return [a,b]


ans=findDifference([1,2,3,3],[1,1,2,2])
print(ans)

'''
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6]. 
'''