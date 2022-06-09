"""
617. Merge Two Binary Trees
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes 
of the two trees are overlapped while the others are not. 
You need to merge the two trees into a new binary tree. 
The merge rule is that if two nodes overlap, then sum node values up 
as the new value of the merged node. Otherwise, the NOT null node will 
be used as the node of the new tree.
Return the merged tree.
Note: The merging process must start from the root nodes of both trees.

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:
The number of nodes in both trees is in the range [0, 2000].
-10^4 <= Node.val <= 10^4
"""

from utils import are_equal
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        l_str = self.left.val if self.left else 'None'
        r_str = self.right.val if self.right else 'None'
        return f"{self.val} ({l_str}, {r_str})"


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def sum_node(nl, nr):
            if nl is None:
                return nr

            if nr is None:
                return nl

            res = TreeNode(nl.val + nr.val)
            res.left = sum_node(nl.left, nr.left)
            res.right = sum_node(nl.right, nr.right)
            return res

        return sum_node(root1, root2)


def build_tree(tree: List[int]) -> Optional[TreeNode]:
    if len(tree) == 0:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in tree]
    for i in range(len(tree)-1, 0, -1):
        if nodes[i] is not None:
            p = (i-1) // 2
            if i % 2 == 0:
                nodes[p].right = nodes[i]
            else:
                nodes[p].left = nodes[i]

    return nodes[0]


def tree_to_list(root: Optional[TreeNode]):
    if root is None:
        return []

    def get_height(node: TreeNode):
        if node is None:
            return 0
        return max(get_height(node.left), get_height(node.right)) + 1

    res = []
    st = [root]
    count = 0
    h = get_height(root)
    while count < 2**(h+1):
        curr = st.pop(0)
        res.append(None if curr is None else curr.val)
        count += 1
        if curr is not None:
            st.append(curr.left)
            st.append(curr.right)
        else:
            st.append(None)
            st.append(None)

    for i in range(len(res) - 1, 0, -1):
        if res[i] is not None:
            break

        res.pop(-1)

    return res


def test_solution():
    sol = Solution()

    def test(root1: List[int], root2: List[int], expected: List[int]):
        res = sol.mergeTrees(build_tree(root1), build_tree(root2))
        are_equal(tree_to_list(res), expected)

    test([], [], [])
    test([1], [], [1])
    test([], [1], [1])
    test([1], [1], [2])
    test([1], [2], [3])
    test([1], [1, 2], [2, 2])
    test([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7])


if __name__ == '__main__':
    test_solution()
