public class j137_exam {
    // 2024
    // 2024
    static int exam(String a , int k){
        int i,j,ct,cf,ans;
        i=j=ct=cf=ans=0;

        while(j<a.length()){
            if(a.charAt(j)=='F')cf++;
            else{

                ct++;
            }j++;

            while(Math.min(cf, ct)>k){
                if(a.charAt(i)=='F'){

                    cf--;
                }
            else 
            {ct--;
            }
            i++;

            }

            ans=Math.max(ans,cf+ct);
        }
        return ans;
    }
    public static void main(String[] args) {
       int res= exam("TTFTTFT", 1);
       System.out.println(res);
    }
}
