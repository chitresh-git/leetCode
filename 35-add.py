def addDigits(num):
      
       
        
   
        while num>10:
            s=0
            
            # print(temp)
            while num!=0:
             r=num % 10
         
             s=s+r
             num=int(num/10)
             print(num)
            
            num=s



        return s
       
           
        

ans=addDigits(38)
temp=38
s=0
print(ans)