def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l=len(strs)
        outer=strs[0]
        outer=str(outer)
        data=[""]
        
        sum=""
        ind=0
        for e in outer:
                count=0
                
                for i in range(l):
                  print(i,ind)
                  if ind==i:
                        s=strs[i]
                        print(s)
                        if s.find(e)!=-1:
                                count+=1
                                print(count)
                                if count==l:
                                        sum=sum+e
                                        print(sum)
                                        data.append(sum)
                                        e=sum
                        else:
                                sum=""
                                break
                ind+=1
        
        return data





d=longestCommonPrefix(["flower","flow","flight"])
print(d)
max=max(d)
print(max)