def gcdOfStrings(str1, str2):
        # NOT DONE 
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1,str2=str(str1),str(str2)

        if str1>str2:
                short=str2
        else:
                short=str1

        
        flag=True
        i=0
        result=""

        while flag:
            try:
                if short[i] in str1 and short[i] in str2:
                        result=result+short[i]
                        flag=True
                        i+=1
                else:
                      flag=False
            except:
                        
                flag=False
        
       
        
        result=list(set(result))
        result.reverse()


        result="".join(result)
        
        return (result)

ans=gcdOfStrings("ABABAB","ABAB")



print(ans)


