def pal (n):
 if n<=100:
   return False
 else:
   m=n
   sum=0
   r=0
   while(n!=0):     #   121   12   1    
      r=n%10        #   1     2    1
      sum=sum*10+r  #   1     12   121 
      n=int(n/10)   #   12    1     0
    #   print(n,sum)
   if m==sum:
      return True
   else :
      return False
    

num=int(input("enter any interger"))
print(pal(num))

