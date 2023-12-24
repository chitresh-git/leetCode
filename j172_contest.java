
class Solution {


    public int largestPerimeter(int[] nums) {

        int perimeter = 0;
        int temp = 0;
        perimeter += nums[0];
        int sides = 1;

        for (int i = 1; i < nums.length; i++) {
            temp += nums[i - 1];

            if (temp >= nums[i]) {
                perimeter += nums[i];
                sides++;

            }
        }

        if (sides >= 3)
            return perimeter;
        else
            return -1;

    }
}

public class j172_contest {
    public static void main(String[] args) {
        Solution s = new Solution();
        int a[] = { 5,5,5};
        System.out.println(s.largestPerimeter(a));
    }
}
