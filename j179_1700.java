public class j179_1700 {
    
}
/* 
 * class Solution {
    public int countStudents(int[] std, int[] sand){
      int len=std.length;
      int st[]=new int[len*10];
      for(int i=0;i<len;i++){
          st[i]=std[i];
      }
    
     
     int front , rear, top,swap;
        swap=top=front=0;
        rear=len-1;
      
        while(front<=rear){
           
            if(swap>len)
            return rear-front+1;

            if(st[front]==sand[top]){
                front++;
                top++;
                swap=0;
            }
            else{
                rear++;
                st[rear]=st[front];
                front++;
                swap++;

            }
        }

        return 0;

        
    }
}

/*
       
*/
 