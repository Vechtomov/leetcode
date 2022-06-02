"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import List, Optional
from utils import are_equal

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stored = 0
        res = ListNode()
        prev_node = res
        while l1 != None or l2 != None:
            v1 = l1.val if l1 != None else 0
            v2 = l2.val if l2 != None else 0
            curr = v1 + v2 + stored
            val, stored = curr % 10, curr // 10
            prev_node.next = ListNode(val)
            prev_node = prev_node.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        if stored != 0:
            prev_node.next = ListNode(stored)
        
        return res.next

def test_solution():
    sol = Solution()

    def to_nodes(l: List[int]):
        res = ListNode()
        prev = res
        for v in l:
            prev.next = ListNode(v)
            prev = prev.next
        return res.next

    def to_list(node: ListNode):
        res = []
        while node is not None:
            res.append(node.val)
            node = node.next
        return res

    def test(l1, l2, expected: List[int]):
        are_equal(to_list(sol.addTwoNumbers(to_nodes(l1), to_nodes(l2))), expected)

    test([0], [0], [0])
    test([1], [2], [3])
    test([9], [8], [7,1])
    test([0, 1], [5], [5,1])
    test([5], [0, 1], [5,1])
    test([2,4,3], [5,6,4], [7,0,8])
    test([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])


if __name__ == '__main__':
    test_solution()
