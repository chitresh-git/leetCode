def dailyTemperatures(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        result=[]
        l=len(temperatures)-1
        for i in range(len(temperatures)-1):
                # print(temperatures[i],i)
                for j in range(i+1,len(temperatures)):
                      
                 
                     
                        if temperatures[j]>temperatures[i]:
                                
                                c=j-i
                                result.append(c)
                                break
                        elif j==l:
                                result.append(0)
                    #   except:
                    #     result.append(0)
        result.append(0)     
                                
        
        return result

ans=dailyTemperatures([73,74,75,71,69,72,76,73])
print(ans)

'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: tempera
'''