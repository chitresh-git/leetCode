public class j136_kth {

    static int[] bubble(int arr[]) {
        int pass = 1;
        boolean f = true; // this condition is use to make bubble sort algo adaptive
        for (int j = 0; j < arr.length - 1; j++) {
            // System.out.println("pass=" + pass);
            for (int i = 0; i < arr.length - j - 1; i++) {

                if (arr[i] > arr[i + 1]) { // comparing the adjacent elements
                    int temp;
                    temp = arr[i];
                    arr[i] = arr[i + 1]; // performing swapping 
                    arr[i + 1] = temp;
                    f = false;

                }
                // show(arr);
            }
            if (f) // if no comparision occur in inner loop then this condition will gets true and
                   // outer loop will get break
                break;
            pass++;
        }
        return arr;
    }
    
    
    static int take(int a [][] , int k){

        int row=a.length;
        // System.out.println(row);
        int col=a[0].length;
        // System.out.println(col);
        

        int arr[]=new int[row*col];
        int i=0;
        for(int[] rows : a){
            for(int ele:rows){
                arr[i]=ele;
                i++;
            }
        }

        arr=bubble(arr);

      return arr[k-1];

    }
    public static void main(String[] args) {
        int arr[][]={{1,2},{1,3}};
        int ans=take(arr,2);
        System.out.println(ans);
        
    }
}


    // public int[] remove(arr[]){
    //     int temp[]=new int[arr.length];
    //     temp[0]=arr[0];
    //     for(int i=1;i<arr.length;i++){
    //         if(arr[i]!=temp[i-1])
    //         temp[i]=arr[i];
    //     }
    //     return temp;
    // }