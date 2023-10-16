def reverse(x):
   
    
        flag=0
        if x <0:
                flag=True
                x=abs(x)
          
        x=str(x)
        
        x=list(x)

   
        x.reverse()
        x="".join(x)
        x=int(x)
        if flag:
                x=-(x)
        
     

        if x> 2**31-1 or x< -2**31:
                return 0
        else: return x
        

      
ans=reverse(-1563847412)
print(ans)