"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-2^31 <= nums[i] <= 2^31 - 1
"""

from utils import are_equal
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = -1
        for i, num in enumerate(nums):
            if num != 0 and j > -1:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            elif num == 0 and j == -1:
                j = i


def test_solution():
    def test(nums: List[int], expected: List[int]):
        sol = Solution()
        sol.moveZeroes(nums)
        are_equal(nums, expected)

    test([0], [0])
    test([1], [1])
    test([1, 0], [1, 0])
    test([0, 1], [1, 0])
    test([0, 1, 0], [1, 0, 0])
    test([0, 0, 1], [1, 0, 0])
    test([0, 1, 0, 2], [1, 2, 0, 0])
    test([0, 0, 1, 2], [1, 2, 0, 0])
    test([0, 1, 0, 2, 0], [1, 2, 0, 0, 0])
    test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])


if __name__ == '__main__':
    test_solution()
