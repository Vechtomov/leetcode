"""
968. Binary Tree Cameras
You are given the root of a binary tree. We install cameras on the tree nodes 
where each camera at a node can monitor its parent, itself, and its immediate children.
Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. 
The above image shows one of the valid configurations of camera placement.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val == 0
"""

from utils import are_equal
from typing import List, Optional
from functools import cache


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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        @cache
        def helper(node, tracked):
            if not node:
                return 0

            counts = []
            b = 1 if tracked == 2 else 0
            
            counts.append(helper(node.left, 1) + helper(node.right, 1) + 1 - b)

            if tracked == 1:
                counts.append(helper(node.left, 0) + helper(node.right, 0))

            if node.left:
                counts.append(helper(node.left, 2) + helper(node.right, b) + 1)

            if node.right:
                counts.append(helper(node.left, b) + helper(node.right, 2) + 1)

            if node.left and node.right:
                counts.append(helper(node.left, 2) + helper(node.right, 2) + 2)

            return min(counts)

        return helper(root, 0)


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

    def test(tree: List[int], expected: int):
        sol = Solution()
        rood = sol.minCameraCover(build_tree(tree))
        are_equal(rood, expected)

    test([], 0)
    test([0], 1)
    test([0, None, None], 1)
    test([0, 0, None, 0, 0], 1)
    test([0, 0, 0, 0, 0, 0, 0], 2)
    test([0, 0, 0, 0, 0, 0, 0, 0], 3)
    test([0, 0, 0, 0, 0, 0, 0, 0, None, 0], 3)
    test([0, 0, None, 0, None, None, None, 0], 2)


if __name__ == '__main__':
    test_solution()
