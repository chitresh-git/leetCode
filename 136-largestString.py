def maximumValue(strs):
        """
        :type strs: List[str]
        :rtype: int
        2496
        """
        ans=[]
        for s in strs:
            if(s.isnumeric()):
                  t=int(s)
                  print(t)
                  ans.append(t)
        
            else:
                  ans.append(len(s))
            
        print(max(ans))
        return (max(ans))

maximumValue(["1","01","001","0001"])
                  
        