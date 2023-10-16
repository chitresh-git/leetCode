class Linked {
    // 206 solved
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

    void show(Node head) {
        Node n = head;

        while (n.next != null) {
            System.out.print(" " + n.data);
            n = n.next;
        }
        System.out.print(" " + n.data + "\n");
    }



    Node reverse;
    Node rev(int data){
        Node node=new Node(data);
    
            node.next=reverse;
            reverse=node;
        

        return reverse;
    }
     Node reverseList() {
         Node n=head;
         Node answer=null;
         while(n!=null){
            answer= rev(n.data);
             n=n.next;
         }
         return answer;
        }
}

public class j146_reversedLL {
    public static void main(String[] args) {
        Linked list=new Linked();
        list.fill();
        list.show(list.head);
        list.reverseList();
        list.show(list.reverse);
    }
}
