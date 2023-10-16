class Linked {
    // 83 solved
    Node head;

    class Node {
        int data;
        Node next;

        Node(int val) {
            data = val;
            next = null;
        }
    }

    void insert(int val) {
        Node node = new Node(val);

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
        for (int i = 8; i >= 0; i = i - 2) {
            insert(i);
        }
        insert(0);
        insert(-1);
        insert(-1);
    }

    void show() {
        Node n = head;

        while (n.next != null) {
            System.out.print(" " + n.data);
            n = n.next;
        }
        System.out.print(" " + n.data + "\n");
    }
     int deleteDuplicates() {
       

        Node current=head;
        if(head==null){
            return 0;
        }
        Node forward=head.next;

        while(current.next!=null){
            if(current.data==forward.data){
                current.next=forward.next;
                forward=forward.next;

            }
            else{
                current=current.next;
                forward=forward.next;

            }

        }
        show();
        return 0;

        
    }
}


public class j144_duplicateNode {
public static void main(String[] args) {
    Linked list=new Linked();
    list.fill();
    list.show();
    list.deleteDuplicates();
    }
}
/*
 * Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
 */
