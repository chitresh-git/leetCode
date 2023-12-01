public class rdemo {

   static int cal(int N, int V , int X){

        int time=0;

        if(V*3<=N){
            time=V*3*X;
            time+=V*X;
        }
        else{
          time=V*X;
          time+=N*X;
        }

        return time+X;
    }
    public static void main(String[] args) {
        System.out.println(cal(15, 2, 10));
    }
}
