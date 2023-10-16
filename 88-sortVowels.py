def sortVowels(s):
        """
        :type s: str
        :rtype: str
        """

        vowels=["A","E","I","O","U",'a','e','i','o','u']
        svow=[]

        for e in s :
                if e in vowels:
                    svow.append(ord(e))          
        
        svow.sort()
        print(svow)
        txt=""
        i=0
        for e in s:
               if e in vowels:
                      
                      txt+=chr(svow[i])
                      i+=1
               else:
                      txt+=e
        
        return txt


ans=sortVowels("lYmpH")
print(ans)