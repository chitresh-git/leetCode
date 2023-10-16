def maximumNumberOfStringPairs(words):
        """
        :type words: List[str]
        :rtype: int
        """

        l=len(words)
        # l=int(l/2)

        count=0

        for i in words:
            # words.remove(i)
            e=i
            e=list(e)
          
            e.reverse()
            e="".join(e)
            

            if words.count(e)!=0 and i!=e:
                count+=words.count(e)
        
            
        
          

        
        return int(count/2)

ans=maximumNumberOfStringPairs(["sa","ue","ss","df","au","ru","id","ur"])
print(ans)