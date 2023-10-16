def groupThePeople(groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        r=[]
        d={}
        i=0
        temp=[]
        
        while i<len(groupSizes):
                
                if len(temp)<groupSizes[i]:
                        temp.append(i)
                        print(i)
                        i+=1
                
                else:
                        r.append(temp)
                        print(temp)
                        temp.clear()

                
                
           

        print(r)
ans=groupThePeople([3,3,3,3,3,1,3])
print(ans)


                
