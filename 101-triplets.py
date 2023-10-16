def arithmeticTriplets(nums, diff):
        """
        NOT SOLVED 
        
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        res=[]
        for i in range(len(nums)):
                fix=nums[i]
                temp=set()

                for j in range(i+1,len(nums)):
                       
                    
                       
                        if abs(fix-nums[j])==diff:
                                print(abs(fix-nums[j]))
                                
                                # temp.add(i)
                                # temp.add(j)
                                res.append(i)
                                res.append(j)
                                
                                i=j

                

        return int(len(res)/3)


ans=arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2)
print(ans)