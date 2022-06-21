"""
1642. Furthest Building You Can Reach
You are given an integer array heights representing the heights of buildings, 
some bricks, and some ladders.
You start your journey from building 0 and move to the next building by possibly 
using bricks or ladders.
While moving from building i to building i+1 (0-indexed),
If the current building's height is greater than or equal to the next building's 
height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, 
you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the 
given ladders and bricks optimally.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

Constraints:
1 <= heights.length <= 10^5
1 <= heights[i] <= 10^6
0 <= bricks <= 10^9
0 <= ladders <= heights.length
"""

from utils import are_equal
from typing import List
from heapq import heappush, heappop, heapify


class Solution:
    def furthestBuilding(self, h: List[int], bricks: int, ladders: int) -> int:
        d = []
        i = 0
        while i < len(h) - 1:
            diff = h[i+1] - h[i]
            if diff > 0:
                if bricks >= diff:
                    bricks -= diff
                    heappush(d, -diff)
                elif ladders > 0:
                    ladders -= 1
                    if len(d) > 0:
                        max_diff = -d[0]
                        if diff <= max_diff:
                            heappop(d)
                            bricks += max_diff
                            continue
                else:
                    break

            i += 1

        return i


def test_solution():

    def test(h: List[int], bricks: int, ladders: int, expected: int):
        sol = Solution()
        are_equal(sol.furthestBuilding(h, bricks, ladders), expected)

    test([1], 0, 0, 0)
    test([1, 2], 1, 0, 1)
    test([1, 2], 0, 1, 1)
    test([1, 2], 1, 1, 1)
    test([1, 3], 1, 0, 0)
    test([1, 3], 0, 1, 1)
    test([1, 2, 3], 1, 0, 1)
    test([1, 2, 3], 2, 0, 2)
    test([1, 2, 3], 1, 1, 2)
    test([1, 2, 3], 0, 2, 2)
    test([1, 4, 2, 3], 2, 1, 3)
    test([1, 4, 2, 3, 2, 1], 2, 1, 5)
    test([1, 4, 2, 3, 2, 1, 4], 2, 1, 5)
    test([1, 5, 1, 2, 3, 4, 10000], 4, 1, 5)

    test([4, 2, 7, 6, 9, 14, 12], 5, 1, 4)
    test([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7)
    test([14, 3, 19, 3], 17, 0, 3)


if __name__ == '__main__':
    test_solution()
