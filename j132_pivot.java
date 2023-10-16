public class j132_pivot {
    public static int pivotIndex(int[] nums) {

      


        for(int i=0;i<nums.length;i++){
           int right=0;
           int left=0;


            for(int j=i+1;j<nums.length;j++){
                right+=nums[j];
    
            }
            System.out.println(right);
            for(int k=i-1;k>=0;k--){
                     left+=nums[k];
                    
            }

            if(left==right){
                return i;
            }
        }

        return -1;

        
    }

    public static void main(String[] args) {
        int a[]={1,2,3};
        int ans=pivotIndex(a);
        System.out.println(ans);
    }
        
    
}
