def countBalls(lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """

        # time limit exceded 

        res=[]
        count=[]


        for i in range(lowLimit,highLimit+1):
                i=str(i)
                sum=0

                for e in i:
                        sum=sum+int(e)

                
                res.append(sum)
                count.append(res.count(sum))

        
        return max(count)


ans=countBalls(1,10)
print(ans)


"""
Example 1:

Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
Example 2:

Input: lowLimit = 5, highLimit = 15
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.
Example 3:

Input: lowLimit = 19, highLimit = 28
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.
"""