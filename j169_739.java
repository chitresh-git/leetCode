public class j169_739 {
    static void cal(int [] t){
        int a[]=new int[t.length];
        for(int k=t.length-1;k>=0;k--){
            System.out.println("pass"+t[k]);
            for(int i=k-1;i>=0 && t[i]<t[k];i--){
                a[i]=k-i;
                System.out.println(t[i]+" "+a[i]);
            }
        }

        for(int e:a)
        System.out.print(e);
    }
    public static void main(String[] args) {
        int n[]={73,74,75,71,69,72,76,73};
        cal(n);
    }
}
