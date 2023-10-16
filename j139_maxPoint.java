import java.util.Arrays;



public class j139_maxPoint {

  static int getmax(int[] a){
        int m=a[0];
        for(int e:a){
            if(e>m){
                m=e;
            }
        }
        return m;
    }
    
     static int maxWidthOfVerticalArea(int[][] points) {

        int temp[]=new int[points.length];

        for(int i=0;i<points.length;i++){
            temp[i]=points[i][0];

        }

        Arrays.sort(temp);

        for(int i=0;i<temp.length-1;i++){
            temp[i]=temp[i+1]-temp[i];
        }
        temp[temp.length-1]=0;

        int ans=getmax(temp);
        return ans;
        
    }

    public static void main(String[] args) {
        int a[][]={{3,1},{9,0},{1,0},{1,4},{5,3},{8,8}};
        int res=maxWidthOfVerticalArea(a);
        System.out.println(res);
    }
}
