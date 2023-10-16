public class j135_superPalindrome{
// 906
    static int palindrome(int n){
        int copy=n;
        
        int sum=0;
        while(n!=0){
            int r=n%10;
            sum=sum*10+r;
            n=n/10;
        }

        if(copy==sum){
            return 1;
        }
        else
        return 0;
    }

    static int superPalindrome(int left, int right){
        int ans=0;
        for(int n=left;n<=right;n++){
        if(palindrome(n)==1){
            double sqrt=Math.sqrt(n);
            int c=(int)sqrt;

            if(c-sqrt==0){

                System.out.println(n+" "+sqrt);
                ans+=palindrome((int)sqrt);
            }
          
            //  System.out.println((int)sqrt);
            
        }
    }
        return ans;
    }
    public static void main(String[] args) {

       int left=Integer.parseInt("1");
       int right=Integer.parseInt("2");

        int result=superPalindrome(left, right);
        System.out.println(result);

    }
}