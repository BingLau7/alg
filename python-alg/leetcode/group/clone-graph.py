from typing import Set, Mapping


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self._cloneGraph(node, {})

    def _cloneGraph(self, node: 'Node', has_vals: Mapping) -> 'Node':
        if not node:
            return
        if node.val in has_vals:
            return has_vals[node.val]
        if node.val not in has_vals:
            res = Node(node.val, [])
            has_vals[node.val] = res
            for n in node.neighbors:
                res.neighbors.append(self._cloneGraph(n, has_vals))
            return res


def printGroup(node: 'Node', has_vals: Set):
    if node.val in has_vals:
        return
    has_vals.add(node.val)
    if node.neighbors != Node:
        print(node.val, "->", [n.val for n in node.neighbors])
        for n in node.neighbors:
            printGroup(n, has_vals)
    else:
        print(node.val, "->")


if __name__ == '__main__':
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    printGroup(node1, set())
    printGroup(Solution().cloneGraph(node1), set())