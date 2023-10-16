def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

 
        l=len(flowerbed)
        remainingPalces=0

        if flowerbed[0]==1:
                
                for i in range(2,l-1,3):
                        print(i)
                        if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                                remainingPalces+=1
        else:
                    for i in range(1,l-1,3):
                        print(i)
                        if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                                remainingPalces+=1



        if remainingPalces>=n:
                return True
        
        else : 
                return False


ans=canPlaceFlowers([1,0,1],1)
print(ans)

'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flow
'''
