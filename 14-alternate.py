def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1)>len(word2):
                big=word1
               
        else:
                big=word2
               
        
        neword=""
        i,j=0,0
        for e in range(len(big)):
                
                 if len(word1)>i:
                  neword=neword+word1[i]
                  i+=1
        
                

                
                 if len(word2)>j:
                  neword=neword+word2[j]
                  j+=1
                 print(neword)
        
        return (neword)

ans=mergeAlternately("ab","pqrs")
print(ans)


"""
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""
