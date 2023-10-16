class Linked {
    // 2807 solved
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

    Node insertGCM() {
        if(head==null || head.next==null){
            return null;
        }

        Node current = head;
        Node forward = head.next;

        while (forward != null) {
            int Num1 = current.data;
            int Num2 = forward.data;
            int Temp, GCD;

            while (Num2 != 0) { // calculating the gcd 
                Temp = Num2;
                Num2 = Num1 % Num2;
                Num1 = Temp;
            }
            GCD = Num1;

           
            Node node=new Node(GCD); // creating a new node for gcd
            node.next=forward; // inserting the gcd node in between the current and forward nodes
            current.next=node;

            current=current.next.next; // current will move two steps in forward direction (because of new gcd node we have to move two steps for cuurent node )

        }
        return head;

    }
}

public class j145_insertGCM {
    public static void main(String[] args) {
        Linked list=new Linked();
        // list.insert(18);
        // list.insert(6);
        // list.insert(10);
        // list.insert(3);
        list.insert(0);

        list.show();

        list.insertGCM();
        list.show();

    }
}
/*
 * 
            ListNode node=new ListNode(GCD); // creating a new node for gcd
            node.next=forward; // inserting the gcd node in between the current and forward nodes
            current.next=node;

            current=current.next.next; // current will move two steps in forward direction (because of new gcd node we have to move two steps for cuurent node )
 */