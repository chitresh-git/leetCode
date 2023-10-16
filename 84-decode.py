def decodeMessage(key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """

        d=list()

        for i in key:
                if i not in d and i!=" ":
                         d.append(i)
        

     

        txt=""
        
        for i in message:
                if i ==" ":
                        txt+=i
                else:
                 temp = d.index(i)
                 temp+=97
                 txt+=chr(temp)

        
        return txt

     

ans=decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv")

print(ans)