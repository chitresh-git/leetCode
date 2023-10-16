def selfDividingNumbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]

        for n in range(left,right+1):
            m=n
            flag=True
            temp=[]

            if str(n).count("0")==0:


              while n!=0:
                  r=n%10
                  n=int(n/10)
               
                       
                
                  temp.append(r)
            
              for e in temp:
                  if m%e!=0:
                        flag=False
                        break

      
            
              if flag:
                  res.append(m)

            

        return res


ans=selfDividingNumbers(1,22)
print(ans)
                  
                  

                
                