class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(data):
        if data is None or len(data) <= 0:
            return None
        _reverse_data = [i for i in reversed(data)]
        root = ListNode(_reverse_data.pop())
        tmp = root
        while len(_reverse_data) > 0:
            tmp.next = ListNode(_reverse_data.pop())
            tmp = tmp.next
        return root

    def string(self):
        tmp = self
        values = []
        while tmp:
            values.append(tmp.val)
            tmp = tmp.next
        return "->".join([str(s) for s in values])


if __name__ == '__main__':
    a = ListNode.create([1, 2, 3, 4, 5])
    print(a.string())
