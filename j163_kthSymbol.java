public class j163_kthSymbol {
    // my code is correct but takes more time 
    static void myown(int n, int k){
        String row="0";
        String temp="";
        
        for(int i=0;i<n-1;i++){
            for(int s=0;s<row.length();s++){
                if(row.charAt(s)=='0'){
                    temp=temp+"01";
                }
                else{
                    temp=temp+"10";
                }
            }
             row=temp;
            temp="";
        }

       int ans=row.charAt(k-1)-'0';
       System.out.println(row);
       System.out.println(ans);
    }


   static int newCal(int n,int k){
        if(n==1)
        return 0;

        if(k%2!=0) 
        return newCal(n-1, (k+1)/2)==0?0:1; // if k is odd we will return same 
        else
        return newCal(n-1,k/2 )==0?1:0;  // if k is even we perform the complement

    }
    public static void main(String[] args) {
        // myown(10,101);<

        System.out.println(newCal(5,3));
    }
}
