def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """

        l=s.split()
        # l.reverse()
        l=list(l)
      
        newl=[]

        for e in l:
                e=list(e)
                e.reverse()
                e="".join(e)
                newl.append(e)

        newl=" ".join(newl)
        return newl


ans=reverseWords("Let's take LeetCode contest")
print(ans)

 