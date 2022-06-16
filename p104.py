"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def helper(l, r):
            if not l or not r:
                return l == r

            if l.val != r.val:
                return False

            return helper(l.left, r.right) and helper(l.right, r.left)

        return helper(root.left, root.right)


class SolutionIterative:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        st = [root.left, root.right]
        res = True
        while st and res:
            l = st.pop(0)
            r = st.pop(0)
            if not l or not r:
                res = l == r
            elif l.val != r.val:
                res = False
            else:
                st.append(l.left)
                st.append(r.right)

                st.append(l.right)
                st.append(r.left)

        return res


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


def test_solution():

    def test(root1: List[int], expected: bool):
        sol = SolutionIterative()
        tree = sol.isSymmetric(build_tree(root1))
        are_equal(tree, expected)

    test([], True)
    test([1], True)
    test([1, 2], False)
    test([1, 2, 2], True)
    test([1, 2, 3], False)
    test([1, 2, 2, 3], False)
    test([1, 2, 2, 3, 4, 4, 3], True)


if __name__ == '__main__':
    test_solution()
