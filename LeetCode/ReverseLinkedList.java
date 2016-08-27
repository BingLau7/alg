
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class ReverseLinkedList {
    int i = 1;
    /**
     **/
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null){
            return head;
        }
        ListNode p = head;
        ListNode q = head.next;
        ListNode r = q.next;
        ListNode t = null;
        p.next = null;
        while (r != null) {
            t = q;
            q.next = p;
            p = t;
            q = r;
            r = q.next;
        }
        q.next = p;
        return q;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        ListNode t = head.next;
        t.next = new ListNode(3);
        t = t.next;
        t.next = new ListNode(4);
        t = t.next;
        t.next = new ListNode(5);

        ReverseLinkedList r = new ReverseLinkedList();

        ListNode tt = r.reverseList(head);
        while(tt != null) {
            System.out.print(tt.val + " -> ");
            tt = tt.next;
        }
        System.out.println();
    }
}
