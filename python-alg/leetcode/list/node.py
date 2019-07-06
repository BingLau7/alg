

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(*vals):
        if not vals:
            return
        vals = list(vals)
        head_val = vals.pop(0)
        head = ListNode(head_val)
        tmp = head
        for v in vals:
             node = ListNode(v)
             tmp.next = node
             tmp = node
        return head

    @staticmethod
    def toArray(head):
        res = []
        if not head:
            return res
        tmp = head
        while tmp:
            res.append(tmp.val)
            tmp = tmp.next
        return res


if __name__ == '__main__':
    head = ListNode.create(1, 2, 3, 4)
    print(ListNode.toArray(head))
