def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        2108
        """

        for e in words:

            m=e

            e=list(e)
            e.reverse()
          
            e="".join(e)

            if e==m:
                return e
        
        return ""