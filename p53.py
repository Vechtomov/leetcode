"""
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from typing import List
from utils import are_equal


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_s = -float('inf')
        for num in nums:
            if s + num > num:
                s += num
            else:
                s = num
            max_s = max_s if max_s > s else s
        return max_s


class SolutionDivideAndConquer:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_sub(li, ri):
            if li == ri:
                return nums[li], nums[li], nums[li], nums[li]

            if li + 1 == ri:
                l, r = nums[li], nums[ri]
                ml, mr = max(l, l+r), max(r, l+r)
                return ml, mr, max(ml, mr), l+r
            else:
                mi = (li+ri) // 2
                ll, lr, lm, lt = max_sub(li, mi)
                rl, rr, rm, rt = max_sub(mi+1, ri)
                return max(ll, lt+rl), max(rr, lr+rt), max(lm, lr+rl, rm), lt + rt

        return max(max_sub(0, len(nums) - 1))


def test_solution():
    sol = SolutionDivideAndConquer()

    def test(nums: List[int], expected: int):
        are_equal(sol.maxSubArray(nums), expected)

    test([1], 1)
    test([1, 2], 3)
    test([1, -1, 2], 2)
    test([1, -2, 2], 2)
    test([2, -1, 2], 3)
    test([2, -3, 4], 4)
    test([1, -2, 3, -1], 3)
    test([2, -3, 4, -3, 1], 4)
    test([2, -3, 4, -3, 5], 6)
    test([2, -3, 4, -3, 1, -1], 4)
    test([2, -3, 4, -3, 1, 5, -1], 7)
    test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)


if __name__ == '__main__':
    test_solution()
