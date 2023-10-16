def sortSentence(s):
        """
        :type s: str
        :rtype: str
        """

        d,res={},[]
        

        l=s.split()

        for e in l:
                d.update({int(e[-1]):e[:-1]})

        for i in range(1,len(l)+1):
                res.append(d.get(i))
                
        
   
        res=" ".join(res)
        return res

ans=sortSentence("is2 sentence4 This1 a3")
print(ans)