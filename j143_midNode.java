class Linked {
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
    }

    void show() {
        Node n = head;

        while (n.next != null) {
            System.out.print(" " + n.data);
            n = n.next;
        }
        System.out.print(" " + n.data + "\n");
    }
Node mid(Node start,Node last){
    Node slow=start;
    Node fast=start.next;

    while(fast!=last){
        fast=fast.next;
        if(fast!=last){
            slow=slow.next;
            fast=fast.next;

        }

    }
    return slow;
}

void showmid(){
    Node mid=mid(head,null);
    System.out.println(mid.data);
}
}


public class j143_midNode {
    

    public static void main(String[] args) {
        Linked list=new Linked();
        list.fill();
        list.show();
        list.showmid();
        

        
    }
}
