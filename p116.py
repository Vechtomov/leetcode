"""
116. Populating Next Right Pointers in Each Node
You are given a perfect binary tree where all leaves are on the same level, 
and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function 
should populate each next pointer to point to its next right node, just like in Figure B. 
The serialized output is in level order as connected by the next pointers, with '#' 
signifying the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000
"""

from utils import are_equal
from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        l_str = self.left.val if self.left else 'None'
        r_str = self.right.val if self.right else 'None'
        n_str = self.next.val if self.next else 'None'
        return f"{self.val} ({l_str}, {r_str}, {n_str})"


class SolutionStack:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        st = [root]
        res: List[Node] = []
        while len(st) > 0:
            node = st.pop(0)
            res.append(node)
            if node.left is not None:
                st.append(node.left)
                # tree is perfect, each node has 0 or 2 children
                st.append(node.right)

        r = len(res) - 1
        while r > 0:
            beg = r // 2
            for i in range(beg, r):
                res[i].next = res[i+1]
            r = beg - 1

        return res[0]


def build_tree(tree: List[int]) -> Optional[Node]:
    if len(tree) == 0:
        return None

    nodes = [Node(v) if v is not None else None for v in tree]
    for i in range(len(tree)-1, 0, -1):
        if nodes[i] is not None:
            p = (i-1) // 2
            if i % 2 == 0:
                nodes[p].right = nodes[i]
            else:
                nodes[p].left = nodes[i]

    return nodes[0]


def tree_to_list(root: Optional[Node]):
    if root is None:
        return []

    def get_height(node: Node):
        if node is None:
            return 0
        return max(get_height(node.left), get_height(node.right)) + 1

    res = []
    st = [root]
    count = 0
    h = get_height(root)
    while len(st) > 0:
        curr = st.pop(0)
        res.append(curr)
        count += 1
        if curr.left is not None:
            st.append(curr.left)
            st.append(curr.right)

    result = []
    for i in range(len(res)):
        result.append(res[i].val)
        if res[i].next is None:
            result.append('#')

    return result


def test_solution():
    sol = SolutionStack()

    def test(root: List[int], expected: List[int]):
        res = sol.connect(build_tree(root))
        are_equal(tree_to_list(res), expected)

    test([1], [1, '#'])
    test([1, 2, 3], [1, '#', 2, 3, '#'])
    test([1, 2, 3, 4, 5, 6, 7], [1, '#', 2, 3, '#', 4, 5, 6, 7, '#'])


if __name__ == '__main__':
    test_solution()
