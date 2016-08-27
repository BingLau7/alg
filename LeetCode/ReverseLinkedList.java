
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

    public ListNode reverseList(ListNode head, int m, int n){
        if (head == null || head.next == null){
            return head;
        }
        ListNode _head = head;
        ListNode _tail = head;
        for (int i = 0; i < m - 1; i++) {
            _head = _head.next;
        }
        for (int i = 0; i < n - 1; i++) {
            _tail = _tail.next;
        }

        ListNode tail_t = null;
        tail_t = _tail.next;
        _tail.next = null;
        // 接头
        ListNode head_t = head;
        if (m > 2) {
          for (int i = 0; i < m - 2; i++) {
              head_t = head_t.next;
          }
        }
        ListNode head_t_t = reverseList(_head);
        if (m == 1){
            head_t = head_t_t;
            head = head_t_t;
        } else {
            head_t.next = head_t_t;
        }
        // 接尾
        ListNode t = head_t;
        while(t.next != null) {
            t = t.next;
        }
        t.next = tail_t;
        return head;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(3);
        head.next = new ListNode(5);
        // ListNode t = head.next;
        // t.next = new ListNode(3);
        // t = t.next;
        // t.next = new ListNode(4);
        // t = t.next;
        // t.next = new ListNode(5);

        ReverseLinkedList r = new ReverseLinkedList();

        ListNode tt = r.reverseList(head, 1, 2);
        while(tt != null) {
            System.out.print(tt.val + " -> ");
            tt = tt.next;
        }
        System.out.println();
    }
}
