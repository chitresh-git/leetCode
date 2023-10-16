def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        

        # num1=int(num1)
        
        
        num1=list(num1)
        num2=list(num2)
      

        num1=list(map(int,num1))
        num2=list(map(int,num2))
        
        num1.reverse()
        num2.reverse()
        s1,s2=0,0
        print(num1)
        for i in range(len(num1)):
                s1=s1+num1[i]*(10**i)
        print(s1)     
        for i in range(len(num2)):
                s2=s2+num2[i]*(10**i)
                
        
        res=s1+s2
        return res



ans=addStrings("123","12")
print(ans)        