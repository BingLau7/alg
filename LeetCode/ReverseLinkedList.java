
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        return null;
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

        ListNode tt = head;
        while(tt != null) {
            System.out.print(tt.val + " -> ");
            tt = tt.next;
        }
        System.out.println();
    }
}
