
def merge(nums1,nums2):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        def removezero(nums1):
            nums1.reverse()
            i=0
            for e in range(len(nums1)):
                 print(i)
                 print(nums1[i])
                 if nums1[i]==0:
                      del nums1[i]
                      i+=1
                 else:
                      break
            return nums1
        a=[-1,0,0,3,3,3,0,0,0]
        r=removezero(a)  
        print(r)
        

             
        nums1=list(nums1)
        # nums2=list(nums2)
        nums1.extend(nums2)
       
        nums1.sort()
        # print(nums1)
        
        if nums1[0]>=0:
                
            nums1.reverse()
            l=nums1.count(0)
            for e in range(l):
                nums1.remove(0)
        
            nums1.reverse()
        
            return nums1
        else:
             return nums1
    


a=[-1,0,0,3,3,3,0,0,0]
b=[2,5,6]
res=merge(a,b)
print(res)