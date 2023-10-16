public class j134_sortColors {
    public static int[] sortColors(int[] nums) {
        for(int i=0;i<nums.length-1;i++){

            boolean f=true;
            for(int j=0 ;j<nums.length-i-1;j++){
                 if(nums[j]>nums[j+1]){
                    int temp;
                    temp=nums[j];
                    nums[j]=nums[j+1];
                    nums[j+1]=temp;
                    f=false;
                 }
                 show(nums);
                 
            }
            if(f)
            break;
        }

        return nums;

        
    }

    static void show(int a[]){
        for(int ele : a){
            System.out.print(ele);
        }
        System.out.println("\n");
    }

    public static void main(String[] args) {
        int a[]={2,0,2,1,1,0};
        a=sortColors(a);
        show(a);
       
    }
}
