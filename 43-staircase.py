def arrangeCoins(n):
        """
        :type n: int
        :rtype: int
        """
        sum,i,count=0,1,0
        
        

        while n>sum:
                m=sum
                sum=sum+i
                print(sum,i,sum-m)
                if n>=sum:
                        count+=1
                else:
                        return count

                i+=1
        return count

ans=arrangeCoins(53)
print(ans)

'''
Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
'''
                
                