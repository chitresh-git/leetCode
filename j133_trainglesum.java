public class j133_trainglesum {
    public static int triangularSum(int[] nums) {

   

        for(int j=0;j<nums.length-1;j++){
           
            for(int i=0;i<nums.length-j-1;i++){
          
             nums[i]=(nums[i]+nums[i+1])%10;

            }

            nums[nums.length-j-1]=0;


        }

        return nums[0];

      


    }
    public static void main(String[] args) {
        int arr[]={1,2,3,4,5};

        int ans=triangularSum(arr);
        System.out.println(ans);
    }
}
