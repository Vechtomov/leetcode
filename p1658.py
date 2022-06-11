"""
1658. Minimum Operations to Reduce X to Zero
You are given an integer array nums and an integer x. In one operation, you can 
either remove the leftmost or the rightmost element from the array nums and subtract 
its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, 
otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two 
elements (5 operations in total) to reduce x to zero.
 
Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
"""

from bisect import bisect_left
from utils import are_equal
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        def cumsum(arr):
            res = [0] * len(nums)
            cum = 0
            for i, v in enumerate(arr):
                cum += v
                res[i] = cum

            return res

        sum_left = [0] + cumsum(nums)
        sum_right = [0] + cumsum(reversed(nums))

        res = float('inf')
        for i, s in enumerate(sum_left):
            rest = x - s
            if rest < 0:
                break
            hi = len(nums) + 1 - i
            j = bisect_left(sum_right, rest, 0, hi)
            if j != hi and sum_right[j] == rest:
                res = min(res, i + j)

        return res if res < float('inf') else -1

# This solution didn't pass time limit
class SolutionDP:
    def minOperations(self, nums: List[int], x: int) -> int:
        dp = {}

        def remove(l, r, cx):
            if (l, r) in dp:
                return dp[(l, r)]

            if cx == 0:
                dp[(l, r)] = 0
            elif cx < 0 or l > r or l > len(nums) - 1 or r < 0:
                dp[(l, r)] = float('inf')
            else:
                lcount = remove(l + 1, r, cx - nums[l])
                rcount = remove(l, r - 1, cx - nums[r])
                dp[(l, r)] = min(lcount, rcount) + 1

            return dp[(l, r)]

        res = remove(0, len(nums) - 1, x)
        return res if res < float('inf') else -1


def test_solution():
    # sol = SolutionDP()
    sol = Solution()

    def test(nums: List[int], x: int, expected: int):
        are_equal(sol.minOperations(nums, x), expected)

    test([1], 1, 1)
    test([1], 2, -1)
    test([1, 2], 2, 1)
    test([1, 2], 3, 2)
    test([1, 2], 4, -1)
    test([1, 2, 4], 3, 2)
    test([1, 2, 3, 4], 5, 2)
    test([1, 2, 3, 4], 6, 3)
    test([1, 2, 3, 2, 4], 6, 2)

    test([1, 1, 4, 2, 3], 5, 2)
    test([5, 6, 7, 8, 9], 4, -1)
    test([3, 2, 20, 1, 1, 3], 10, 5)


if __name__ == '__main__':
    test_solution()
