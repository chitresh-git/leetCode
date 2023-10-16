def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        out=[]
        inn=[1]
        for i in range(numRows):
                
                
                for j in range(len(inn)):
                        
                        # inn[j]=inn[j]
                        sum=inn[j]+inn[j+1]
                        inn[j+2]=inn[j+1]
                        inn[j+1]=sum
                        
                out.append(inn)


        return out

ans=generate(3)
print(ans)

                