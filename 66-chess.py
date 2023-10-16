def squareIsWhite(coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        l=list(coordinates)
        
        sum=ord(l[0])+ int(l[1])

        if sum%2==0:
                return False
        else :
                return True
        
        


ans=squareIsWhite("a1")
print(ans)


"""
Example 1:

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
Example 2:

Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
Example 3:

Input: coordinates = "c7"
Output: false
"""