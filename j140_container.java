public class j140_container{
    // 11
    // passed but time limit exceeded 

    static int getmax(int a[]){ // this will return max element of array 
        int m=a[0];
        for (int e:a){
            if(e>m){
                m=e;
            }
        }
        return m;
    }
   static int  container(int a[]){

        int l , b, k=0,max=0;
        int n=a.length;
        int ans=0;
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
            b=j-i;
            if(a[i]<=a[j]){
                l=a[i];
            }
            else{
                l=a[j];
            }
            ans=b*l;
            if(ans>max){
                max=ans;
            }
            

            }

        }

        return max;
    }
    public static void main(String[] args) {

        int a[]={1,8,6,2,5,4,8,3,7};
        System.out.println(container(a));
        
    }
}