def numberOfBeams(bank):
        """
        :type bank: List[str]
        :rtype: int
        """
     
 
        sum=0

        l=[]

        for e in bank:
                ones=e.count("1")
                if ones!=0:
                 l.append(ones)
                
        
        for i in range(len(l)-1):
                # if l[i]!=0 and l[i+1]!=0:
                        sum=sum+ (l[i]*l[i+1])
        
        return sum

ans=numberOfBeams(["011001","000000","010100","001000"])
print(ans)


