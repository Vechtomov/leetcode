"""
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""

from typing import List
from utils import are_equal


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        pos = 0
        swap_pos = 0
        for _ in range(len(nums)):
            new_pos = pos + k
            if new_pos >= len(nums):
                new_pos -= len(nums)
            nums[swap_pos], nums[new_pos] = nums[new_pos], nums[swap_pos]
            pos = new_pos
            if pos == swap_pos:
                swap_pos += 1
                pos = swap_pos


class SolutionReverse:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)


def test_solution():
    sol = SolutionReverse()

    def test(nums: List[int], k: int, expected: List[int]):
        sol.rotate(nums, k)
        are_equal(nums, expected)

    test([1], 1, [1])
    test([1], 2, [1])
    test([1, 2], 1, [2, 1])
    test([1, 2], 2, [1, 2])
    test([1, 2], 3, [2, 1])
    test([1, 2], 4, [1, 2])
    test([1, 2, 3], 1, [3, 1, 2])
    test([1, 2, 3], 2, [2, 3, 1])
    test([1, 2, 3], 3, [1, 2, 3])
    test([1, 2, 3, 4], 2, [3, 4, 1, 2])
    test([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])


if __name__ == '__main__':
    test_solution()
