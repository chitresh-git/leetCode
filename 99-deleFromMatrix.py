def deleteGreatestValue(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid=list(grid)
   
        sum=0
        prev=0

        while len(grid)!=0:

          for outer in grid:
                
                if len(outer)==0:
                      return sum
                
                m=max(outer)
                print(m)
                outer.remove(m)
                
                if m>=prev:
                        sum+=m

                prev=m

        return sum

ans=deleteGreatestValue([[10]])
print(ans)
                
               
                        
                