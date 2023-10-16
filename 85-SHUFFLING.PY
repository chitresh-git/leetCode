def restoreString(s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        d={}
        txt=""

        for e,i in zip(s,indices):
                d.update({i:e})
        
        indices.sort()

        for i in indices:
                txt+=d.get(i)
        
        return txt
                

ans=restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])
print(ans)