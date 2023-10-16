def duplicateZeros(arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        arr=list(arr)
        copy=arr.copy()
        print(copy)
        for i in range(len(copy)):
                
                if copy[i]==0:
                        print(copy[i],i)
                        arr.insert(i+1,0)
        
        print(arr)
        arr=arr[:len(copy)]
        return arr

ans=duplicateZeros([0,1,7,6,0,2,0,7])
print(ans)