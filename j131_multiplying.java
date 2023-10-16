import java.util.Arrays;

class j131_multiplying{
    public static int findFinalValue(int[] nums, int original) {
        int demo=original;
for(int i=0 ; i<nums.length;i++){


            System.out.println("nums"+nums[i]);
            System.out.println("demo"+demo);
            if(demo==nums[i]){
                demo=nums[i]*2;
                
                i=-1;
                System.out.println(demo);
            }
        
        }

        return demo;
        
    }
    

    public static void main(String[] args){
        int a[]={8,19,4,2,15,3};
        System.out.println(findFinalValue(a,2));
        int b[]={12,3,4,5};
        b[4]=2;
        System.out.println(b[1]);
        int capa=13,i=0;
        int q[]=new int [12];
    }
}

