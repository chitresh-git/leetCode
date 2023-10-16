import java.util.Arrays;
class deleteSame_130{
    static int minimumOperations(int[] nums) {
       Arrays.sort(nums);
    //    System.out.println(nums);
    int count =0;
       for(int i=0;i<nums.length;i++){
        int m=nums[i];
        if(nums[i]!=0){
            
            for(int j=i;j<nums.length;j++){
                // System.out.println(nums[j]);
             
                nums[j]=nums[j]-m;
            }
     
                count++;

        }
        System.out.println();
       }

      
       return count;
        
    }
    public static void main(String[] args){
        int a[]={1,5,0,3,5};
      
        System.out.println(minimumOperations(a));
    }
}