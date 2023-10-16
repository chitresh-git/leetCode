
class Linked {
    // 2130 solved
    Node head;

    class Node {
        int data;
        Node next;

        Node(int val) {
            data = val;
            next = null;
        }
    }

    void insert(int data) {
        Node node = new Node(data);

        if (head == null) {
            head = node;
        } else {
            Node n = head;
            while (n.next != null) {
                n = n.next;
            }
            n.next = node;
        }
    }

    void fill() {
        for (int i = 0; i<10; i++) {
            insert(i);
        }
       
    }

    void show(Node head) {
        Node n = head;

        while (n.next != null) {
            System.out.print(" " + n.data);
            n = n.next;
        }
        System.out.print(" " + n.data + "\n");
    }

    int getmax(int a[]){ // this method will return max element from the calculted array 
        int m=a[0];
        for(int e:a){
            if(e>m){
                m=e;
            }
        }
        return m;
    }

    int count(Node head){ // determining the length of array 
        Node n=head;
        int count=0;
        while(n!=null){
            count++;
            n=n.next;
        }
        return count;
    }
    int [] cal(Node head, int a[],int len){ // calculating the sum of twin nodes and storing it in array 
        Node n=head;
        int i=0,counter=0;
        while(n!=null){
                  

            a[i]=a[i]+n.data;
            n=n.next;
            counter++;
            if(counter<=len){
            i++;
            }
            if(counter>=len){
                i--;
            }
        }
        return a;
    }
    public int pairSum(Node head) {
        int len=count(head);
        len=len/2; // creating the array of half as size of total length of linked list
        int arr[]=new int[len];
        arr=cal(head,arr,len);
       
        int ans=getmax(arr);
        return ans;

        
    }
}
public class j150_twinsum {
    public static void main(String[] args) {
        Linked list=new Linked();
        list.fill();
        list.show(list.head);
        System.out.println(list.pairSum(list.head));

        
    }
    
}

/*
 * In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
 */