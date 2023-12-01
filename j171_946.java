public class j171_946{
  static  int size=0;
  static  int a[];
  static  int top=-1;

  static void show(){
    for(int e: a){
        System.out.print(e);
    }
    System.out.println();
  }

       static  boolean isEmpty(){
        if(top<0){
           
            return true;
        }
        else
              return false;     
    }

   static  boolean isFull(){
        if(top>=size-1){
           
            return true;
        }
        else
         return false;
    }

    public static void CustomStack(int maxSize) {
        size=maxSize;
     a=new int[size];
    }
    
    public static void push(int x) {
        if(isFull())
        return ;
        else{
            a[++top]=x;
           
        }
        
    }
    
    public static int pop() {
        if(isEmpty())
        return -1;
        else{
            return a[top--];

        }
        
    }
    public static int getTop() {
        if(isEmpty())
        return -1;
        else{
            return a[top];

        }
        
    }
    public static void main(String[] args) {
        int pushed[]={2,1,0};
        int poped[]={1,2,0};

        int len=pushed.length;

        CustomStack(len);
        int i=0,j=0;

        for(i=0;i<len;i++){
            push(pushed[i]);
            System.out.println("poped[j]"+poped[j]+" gettop"+getTop());
            while(j<len && getTop()==poped[j] ){
                // System.out.println("topval"+a[top]);
                pop();
               
                j++;
            }
            show();
        }
        // System.out.println("top"+top);

        System.out.println("j"+j);
        show();


        for(;j<len;j++){
            System.out.println(getTop()+"this"+poped[j]);
            if(getTop()==poped[j]){
                pop();
               
            }
            else{
                System.out.println("false");
                return;
            }
        }

        System.out.println("true");
    }
}