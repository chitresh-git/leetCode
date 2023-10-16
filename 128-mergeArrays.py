def mergeArrays(nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        2570
        """

        nums1.extend(nums2)
        nums1.sort()     

        res=[]
        i=0

        while i < (len(nums1)-1):
                 t=0
              
                 if nums1[i][0]==nums1[i+1][0]:
                        t=[nums1[i][0],nums1[i][1]+nums1[i+1][1]]
                        res.append(t)
                        i+=2
                 else:
                        res.append(nums1[i])
                        i+=1
             
                        
        if res[-1][0]==nums1[-1][0]:
                return res
        else:
                res.append(nums1[-1])
                return res

print(mergeArrays(nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1],[7,2]]))