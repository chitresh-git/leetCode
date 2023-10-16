def checkIfPangram(sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        ascii=[]

        for e in sentence:
                
                ascii.append(ord(e))

        # ascii.sort()
        # print(ascii)
        
        for i in range(97,123):
                if i not in ascii:
                        return False
        
        return True

ans=checkIfPangram("thequickbrownfoxjumpsoverth")

print(ans)
                