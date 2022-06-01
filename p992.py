"""
992. Subarrays with K Different Integers
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: 
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: 
[1,2,1,3], [2,1,3], [1,3,4].

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length
"""

from typing import List
from utils import are_equal
from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(K):
            count = Counter()
            res = i = 0
            for j in range(len(nums)):
                if count[nums[j]] == 0: K -= 1
                count[nums[j]] += 1
                while K < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0: K += 1
                    i += 1
                res += j - i + 1
            return res
        
        return at_most_k(k) - at_most_k(k - 1)



def test_solution():
    sol = Solution()

    def test(nums: List[int], k: int, expected: int):
        are_equal(sol.subarraysWithKDistinct(nums, k), expected)

    test([1], 1, 1)
    test([1], 2, 0)
    test([1,1], 1, 3)
    test([1,2], 1, 2)
    test([1,2], 2, 1)
    test([1,2], 3, 0)
    test([1,2,1,2,3], 2, 7)
    test([1,2,1,3,4], 3, 3)


if __name__ == '__main__':
    test_solution()
